from .context import CT_MANAGER
from .repair import RP_MANAGER
from .goto import with_goto

from .transform import transform, TRANSFORM_REGISTRY

#from .liveupdate import Update, UpdateManager, Redefine, Instrument

from loguru import logger
from pathlib import Path
import time
import shutil


log_file = Path.cwd()/"experiment_record.log"

with log_file.open('w') as f:
    f.write('')

logger.add("experiment_record.log")

logger.info("Program Begin")

def log_program_end(value=''):
    if value != '':
        value = ' with Quality Measure ' + str(value)
    logger.info("Program End"+value)
    if 'REPEAT_ACTIONS' in TRANSFORM_REGISTRY:
        log_file = Path.cwd()/"experiment_record.log"
        repeat_file = Path.cwd()/("experiment_record_"+str(time.time())+".log")
        shutil.copyfile(log_file, repeat_file)