import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
os.system("rm -rf ./daifu_workspace")
os.system("rm -f experiment_record.log.lock")
os.system("torchrun --standalone --nproc_per_node=4 train_with_daifu.py")

os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
os.system("rm -rf ./daifu_workspace")
os.system("rm -f experiment_record.log.lock")
os.system("torchrun --standalone --nproc_per_node=4 train_with_default_checkpoints.py")

os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
os.system("rm -rf ./daifu_workspace")
os.system("rm -f experiment_record.log.lock")
os.system("torchrun --standalone --nproc_per_node=4 train_with_daifu_normal_runs.py")

for i in range(2):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("torchrun --standalone --nproc_per_node=4 train_with_daifu.py")

for i in range(2):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("torchrun --standalone --nproc_per_node=4 train_with_default_checkpoints.py")

for i in range(2):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("torchrun --standalone --nproc_per_node=4 train_with_daifu_normal_runs.py")
