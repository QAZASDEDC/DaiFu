import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from pathlib import Path
checkfreq_path = Path.cwd()/'checkfreq_workspace'


for i in range(3):
    os.system("ps -aux | grep test_daifu_on_py311 | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python finetune/llama_adapter_with_default_checkpoints.py")