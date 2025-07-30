import os
# Don't set CUDA_VISIBLE_DEVICES yet

import tensorflow as tf
# import torch

print("=== TensorFlow GPU Status ===")
# print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPUs available:", tf.config.list_physical_devices('GPU'))

# print("\n=== PyTorch GPU Status ===")
# print("PyTorch version:", torch.__version__)
# print("CUDA available:", torch.cuda.is_available())
# print("CUDA version:", torch.version.cuda if torch.cuda.is_available() else "N/A")
# print("GPU count:", torch.cuda.device_count())

print("\n=== Environment ===")
print("CUDA_VISIBLE_DEVICES:", os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set'))