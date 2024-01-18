import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

#model_arch = "resnet152"



from pathlib import Path
checkfreq_path = Path.cwd()/'checkfreq_workspace'
#print(list(checkfreq_path.glob('*.chk')))
#print(len(list(checkfreq_path.glob('*.chk'))))
#for i in range(3):
#checkfreq will cause resource leak


model_arch = "swin_b"
for i in range(3):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -rf ./checkfreq_workspace")
    os.system("rm -f experiment_record.log.lock")
    return_val = os.system("python main_with_checkfreq.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")
    while return_val != 0:
        os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
        os.system("touch experiment_record.log.lock")
        if len(list(checkfreq_path.glob('*.chk'))) > 0:
            return_val = os.system("python main_with_checkfreq.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --resume True --epoch 3")
        else:
            return_val = os.system("python main_with_checkfreq.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")


for i in range(3):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python main_with_default_checkpoints.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")

for i in range(3):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python main_with_daifu.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")

