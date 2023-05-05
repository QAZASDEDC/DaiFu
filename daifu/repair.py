from .context import CT_MANAGER
from .transform import TRANSFORM_REGISTRY
from . import transform
import traceback
import pdb
import inspect
from pathlib import Path
import shutil
from difflib import SequenceMatcher
from bidict import bidict
import code
import sys
from loguru import logger
import better_exceptions


class Repair():
    def __init__(self, frame_summary, exception):
        self.frame_summary = frame_summary
        self.exception = exception


class DaiFuDebugger(pdb.Pdb):
    def do_describe(self, arg):
        original_func_name = '_'.join(
            RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])

        original_func_file = Path.cwd()/'daifu_workspace' / \
            ('(original)'+original_func_name+'.py')

        with original_func_file.open('r') as f:
            lines = f.readlines()

        faulty_cell_name = RP_MANAGER.get_current().frame_summary.name
        faulty_lineno = RP_MANAGER.get_current().frame_summary.lineno

        faulty_cell_name_items = faulty_cell_name.split('_')
        if faulty_cell_name_items[-2] == 'rest':
            faulty_cell_name_items[-2] = 'cell'
            faulty_cell_name = '_'.join(faulty_cell_name_items)
            faulty_lineno -= 3

        mapping_error_lineno_in_origin_file = TRANSFORM_REGISTRY[original_func_name]['mapping'].inverse[(
            faulty_cell_name, faulty_lineno)][1]

        for lineno, line in enumerate(lines, 1):
            s = str(lineno).rjust(3)
            if len(s) < 4:
                s += ' '
            s += ' '
            if lineno == mapping_error_lineno_in_origin_file:
                s += '>>'
            self.message(s + '\t' + line.rstrip())

        s = 'Err  '
        self.message(s + '\t' + RP_MANAGER.get_current().exception.__repr__())
        #traceback.print_tb(RP_MANAGER.get_current().exception.__traceback__)
        print(better_exceptions.formatter.ExceptionFormatter().format_traceback(RP_MANAGER.get_current().exception.__traceback__)[0])

    def do_focus(self, arg):
        original_func_name = '_'.join(
            RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])

        original_func_file = Path.cwd()/'daifu_workspace' / \
            ('(original)'+original_func_name+'.py')

        surgery_func_file = Path.cwd()/'daifu_workspace' / \
            ('(surgery-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')

        shutil.copyfileobj(original_func_file.open('r'),
                           surgery_func_file.open('w'))

        action_func_file = Path.cwd()/'daifu_workspace' / \
            ('(action-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')

        with action_func_file.open('w') as f:
            f.write('')

        self.message(str(Path.cwd()/'daifu_workspace' /
                     ('(surgery-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')) + ' generaterd.')
        self.message(str(Path.cwd()/'daifu_workspace' /
                     ('(action-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')) + ' generaterd.')

    def do_action(self, arg):
        original_func_name = '_'.join(
            RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])

        action_func_file = Path.cwd()/'daifu_workspace' / \
            ('(action-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')

        try:
            with action_func_file.open('r') as f:
                action_code = f.read()
        except:
            self.message('Action Fails!')
            self.message('Reason: You should create focus first!')
            return

        code.InteractiveInterpreter(transform.globals_envs['_'.join(RP_MANAGER.get_current(
        ).frame_summary.name.split('_')[:-3])]).runsource(action_code, filename=action_func_file, symbol='exec')

        logger.info("Repairing... Action")

    def do_surgery(self, arg):
        original_func_name = '_'.join(
            RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])

        surgery_func_file = Path.cwd()/'daifu_workspace' / \
            ('(surgery-'+str(RP_MANAGER.get_queue_len())+')'+original_func_name+'.py')

        try:
            with surgery_func_file.open('r') as f:
                surgery_code = f.read()
        except:
            self.message('Surgery Fails!')
            self.message('Reason: You should create focus first!')
            return

        faulty_cell_name = RP_MANAGER.get_current().frame_summary.name
        faulty_lineno = RP_MANAGER.get_current().frame_summary.lineno

        faulty_cell_name_items = faulty_cell_name.split('_')
        if faulty_cell_name_items[-2] == 'rest':
            faulty_cell_name_items[-2] = 'cell'
            faulty_cell_name = '_'.join(faulty_cell_name_items)
            faulty_lineno -= 3

        transform.update_code(original_func_name, surgery_code,
                             faulty_cell_name, faulty_lineno)
        
        logger.info("Repairing... Surgery")


class RepairManager():
    def __init__(self):
        self.queue = []
        self.debugger = DaiFuDebugger()
        self.debugger.prompt = '(DaiFu) '
        self.newest_action = 0

    def analyze_current_fault(self):
        current_exception = CT_MANAGER.get_current().exception
        #current_exception = sys.exc_info()[1]
        frame_summaries = traceback.extract_tb(
            current_exception.__traceback__)
        target = 0
        for i, frame_summary in enumerate(frame_summaries):
            if '_'.join(frame_summary.name.split('_')[:-1]).endswith('daifu_cell') or '_'.join(frame_summary.name.split('_')[:-1]).endswith('daifu_rest'):
                target = i
        return Repair(frame_summaries[target], current_exception)

    def get_current(self):
        return self.queue[-1]
    
    def get_queue_len(self):
        return len(self.queue)

    def repair(self):
        self.queue.append(self.analyze_current_fault())
        logger.info("Repair " + str(len(self.queue)) + " Begin")

        original_func_name = '_'.join(
            RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])
        faulty_cell_name = RP_MANAGER.get_current().frame_summary.name
        faulty_lineno = RP_MANAGER.get_current().frame_summary.lineno

        transform.init_rest(original_func_name, faulty_cell_name, faulty_lineno)

        #logger.debug(traceback.format_tb(RP_MANAGER.get_current().exception.__traceback__))
        
        #ONLY For Repeated Experiments
        if 'REPEAT_ACTIONS' in TRANSFORM_REGISTRY:
            self.debugger.reset()
            action = TRANSFORM_REGISTRY['REPEAT_ACTIONS'][self.newest_action]
            if action == 'Action':
                self.debugger.do_action(None)
            elif action == 'Surgery':
                self.debugger.do_surgery(None)
            elif isinstance(action, list):
                for action_per in action:
                    if action_per == 'Action':
                        self.debugger.do_action(None)
                    elif action_per == 'Surgery':
                        self.debugger.do_surgery(None)
            self.newest_action += 1
        else:
            self.debugger.reset()
            self.debugger.interaction(
                None, self.get_current().exception.__traceback__)

        #faulty_cell_name = RP_MANAGER.get_current().frame_summary.name
        #faulty_cell_name_items = faulty_cell_name.split('_')
        #faulty_cell_name_items[-2] = 'rest'
        #rest_cell_name = '_'.join(faulty_cell_name_items)

        logger.info("Repair " + str(len(self.queue)) + " End")
        #return transform.globals_envs['_'.join(RP_MANAGER.get_current().frame_summary.name.split('_')[:-3])][rest_cell_name]


RP_MANAGER = RepairManager()
