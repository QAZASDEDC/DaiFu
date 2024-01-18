import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from pathlib import Path
checkfreq_path = Path.cwd()/'checkfreq_workspace'

os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
os.system("rm -rf ./daifu_workspace")
os.system("rm -rf ./checkfreq_workspace")
os.system("rm -f experiment_record.log.lock")
return_val = os.system("python finetune/llama_adapter_with_checkfreq.py")
while return_val != 0:
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("touch experiment_record.log.lock")
    if len(list(checkfreq_path.glob('*.chk'))) > 0:
        return_val = os.system("python finetune/llama_adapter_with_checkfreq.py --init_from='resume'")
    else:
        return_val = os.system("python finetune/llama_adapter_with_checkfreq.py")
        
for i in range(3):
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python finetune/llama_adapter_with_daifu.py")

for i in range(3):
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python finetune/llama_adapter_with_daifu_normal_runs.py")
    
for i in range(2):
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -rf ./checkfreq_workspace")
    os.system("rm -f experiment_record.log.lock")
    return_val = os.system("python finetune/llama_adapter_with_checkfreq.py")
    while return_val != 0:
        os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
        os.system("touch experiment_record.log.lock")
        if len(list(checkfreq_path.glob('*.chk'))) > 0:
            return_val = os.system("python finetune/llama_adapter_with_checkfreq.py --init_from='resume'")
        else:
            return_val = os.system("python finetune/llama_adapter_with_checkfreq.py")
            
for i in range(3):
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python finetune/llama_adapter_with_checkfreq_normal_runs.py")