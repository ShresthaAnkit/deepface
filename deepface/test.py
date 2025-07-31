import os
# Don't set CUDA_VISIBLE_DEVICES yet
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import tensorflow as tf

print("=== TensorFlow GPU Status ===")
# print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPUs available:", tf.config.list_physical_devices('GPU'))
print("Tensorflow version:", tf.__version__)

print("\n=== Environment ===")
print("CUDA_VISIBLE_DEVICES:", os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set'))