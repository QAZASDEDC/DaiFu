import os
# may need train first to get the checkpoint
# os.system('python cifar10_train.py')
for i in range(10):
    os.system('python cifar10_eval.py')