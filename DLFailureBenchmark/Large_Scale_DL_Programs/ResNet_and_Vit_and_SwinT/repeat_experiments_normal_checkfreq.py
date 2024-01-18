import os

#model_arch = "vit_l_16"

#for i in range(3):
#    os.system("rm -rf ./daifu_workspace")
#    os.system("rm -f experiment_record.log.lock")
#    os.system("python main_normal_runs.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")

model_arch = "vit_l_16"
for i in range(1):
    os.system("ps -aux | grep /home/user/anaconda3/envs/test_daifu_on_ndf_py38/bin/python | grep -v 'grep' | awk '{print $2}'| xargs -I {} kill -9 {}")
    os.system("rm -rf ./daifu_workspace")
    os.system("rm -rf ./checkfreq_workspace")
    os.system("rm -f experiment_record.log.lock")
    os.system("python main_with_checkfreq_normal_runs.py -a " + model_arch + " --dist-url 'tcp://127.0.0.1:9527' --dist-backend 'nccl' --multiprocessing-distributed --world-size 1 --rank 0 --epoch 3")

