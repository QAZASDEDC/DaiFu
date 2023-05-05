import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import tensorflow as tf
import time 
device = '/gpu:0'
with tf.Session() as sess:
    # Select the device
    with tf.device(device):
        # Declare two numbers and add them together in TensorFlow
        a = tf.constant(136)
        b = tf.constant(305)
        result = sess.run(a+b)
        print('Occupying GPU')
while True:
    time.sleep(5)
    print('Occupying GPU')