import tensorflow as tf
import numpy as np
import os
import distutils
#if distutils.version.LooseVersion(tf.__version__) <= '2.0':
#    raise Exception('This notebook is compatible with TensorFlow 1.14 or higher, for TensorFlow 1.13 or lower please use the previous version at https://github.com/tensorflow/tpu/blob/r1.13/tools/colab/fashion_mnist.ipynb')

#(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
print(x_train.shape)
# add empty color dimension
x_train = np.expand_dims(x_train, -1)/255
x_test = np.expand_dims(x_test, -1)/255
# Convert y to one-hot
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
