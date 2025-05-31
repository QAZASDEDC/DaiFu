# Concrete Examples of Deep Learning System Crash Scenarios

Here are concrete examples with code for each crash scenario:

## 1. **API Misuse**
*Description: DL library functions are used incorrectly*

**Example: Integer Division in Batch Size Calculation**
```
# Problematic code in GAN training
def train(self, X_train, epochs=5000, batch = 32, save_interval = 100):
    for cnt in range(epochs):
        # BUG: Using integer division in Python 2 style
        random_index = np.random.randint(0, len(X_train) - batch/2)
        legit_images = X_train[random_index : random_index + batch/2].reshape(batch/2, self.width, self.height, self.channels)
        
        gen_noise = np.random.normal(0, 1, (batch/2, 100))
        syntetic_images = self.G.predict(gen_noise)
        
        x_combined_batch = np.concatenate((legit_images, syntetic_images))
        y_combined_batch = np.concatenate((np.ones((batch/2, 1)), np.zeros((batch/2, 1))))
```

**Issue**: The model's final Dense layer has only 1 output unit with sigmoid activation (designed for binary classification), but CIFAR-10 is a 10-class problem. When using `categorical_crossentropy` loss, it expects the model output to have 10 units to match the number of classes, causing a shape mismatch error: `ValueError: Shapes (None, 1) and (None, 10) are incompatible`.

## 2. **Tensor Mismatch**
*Description: Tensor shapes or data types are incompatible*

**Example: Output Shape Mismatch in Classification**
```
from keras import layers
from keras import models
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
# BUG: Output layer has 1 unit but CIFAR-10 has 10 classes
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='categorical_crossentropy',  # Expects 10 classes
              optimizer='sgd',
              metrics=['accuracy'])

# This will fail: y_train has shape (50000, 1) with values 0-9
# but model outputs shape (batch_size, 1) and loss expects (batch_size, 10)
model.fit(x_train, y_train, epochs=20, batch_size=128)
```

**Issue**: The division `(self.width * self.height * self.channels)/2` produces a float in Python 3, but Dense layers expect integer units, causing shape incompatibility errors.

## 3. **Resource Bug (Out of Memory)**
*Description: Excessive GPU memory allocation is required*

**Example: Oversized Neural Network Layer**
```
# Intentionally large value to trigger OOM
LARGE_ENOUGH_VALUE_AS_AN_INJECTED_FAULT = torch.cuda.get_device_properties(0).total_memory//26632

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        # BUG: Extremely large linear layer causing OOM
        self.fc1 = nn.Linear(9216, LARGE_ENOUGH_VALUE_AS_AN_INJECTED_FAULT)
        self.fc2 = nn.Linear(LARGE_ENOUGH_VALUE_AS_AN_INJECTED_FAULT, 10)
```

**Issue**: The fully connected layer `fc1` has an enormous number of parameters (calculated to consume most GPU memory), causing `CUDA out of memory` errors during model initialization or training.

## 4. **GPU Contention**
*Description: Hosted GPUs are occupied by other programs*

**Example: GPU Resource Blocking Script**
```
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import tensorflow as tf
import time 

device = '/gpu:0'
with tf.Session() as sess:
    with tf.device(device):
        a = tf.constant(136)
        b = tf.constant(305)
        result = sess.run(a+b)
        print('Occupying GPU')
        
# BUG: Infinite loop keeping GPU session active
while True:
    time.sleep(5)
    print('Occupying GPU')
```

**Issue**: This script creates a TensorFlow session that occupies GPU:0 indefinitely, preventing other programs from accessing the GPU and causing `RuntimeError: CUDA out of memory` or device allocation failures.

## 5. **Path Problem**
*Description: Specified file or directory paths are incorrect*

**Example: Incorrect Checkpoint Path**
```
def main():
    # ... training code ...
    
    if args.save_model:
        # BUG: Saving to non-existent directory
        torch.save(model.state_dict(), "checkpoint/mnist_cnn.pt")
```

**Issue**: The code attempts to save the model to `"checkpoint/mnist_cnn.pt"` but the `checkpoint` directory doesn't exist, causing `FileNotFoundError: [Errno 2] No such file or directory`.

## 6. **Exceptional Data**
*Description: The input data are unexpected or anomalous*

**Example: NaN Values in Training Data**
```
augment_call_times = 0

def augment(item):
    global augment_call_times
    augment_call_times += 1
    if augment_call_times == 5000:
        import numpy as np
        # BUG: Injecting NaN values into training data
        return torch.full_like(item, np.nan).to(torch.float64)
    else:
        return item

def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data = augment(data)  # Potentially corrupted data
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)  # Will produce NaN loss
        loss.backward()
        optimizer.step()
```

**Issue**: The function encounters tensors with NaN values, causing the function to throw exception.

## 7. **Runtime Error (Non-Deterministic)**
*Description: Temporary issues like GPU device disconnection, transient file I/O errors, and distributed communication faults occur*

**Example: File I/O Operations During Training**
```
import torch
import torch.nn as nn
import os
import random
import time

def save_checkpoint(model, epoch, filepath):
    """Save model checkpoint with potential I/O failures"""
    try:
        # BUG: I/O operation that may fail due to disk issues, permissions, or concurrent access
        if random.random() < 0.2:  # 20% chance of I/O failure
            raise OSError("Disk full or permission denied")
        
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
        }, filepath)
        print(f"Checkpoint saved at epoch {epoch}")
    except OSError as e:
        print(f"Failed to save checkpoint: {e}")
        raise

def load_training_data(data_path):
    """Load training data with potential file access issues"""
    try:
        # BUG: File may be locked by another process or temporarily unavailable
        if random.random() < 0.15:  # 15% chance of file access failure
            raise PermissionError("File is locked by another process")
        
        # Simulate file reading
        time.sleep(0.1)  # Simulate I/O delay
        return torch.randn(1000, 784)  # Simulated data
    except PermissionError as e:
        print(f"Data loading failed: {e}")
        raise

def train_with_io_operations():
    model = nn.Linear(784, 10)
    
    for epoch in range(100):
        try:
            # BUG: Loading data may fail due to file system issues
            data = load_training_data(f"data/batch_{epoch}.pt")
            
            # Training step
            output = model(data)
            loss = nn.functional.mse_loss(output, torch.randn(1000, 10))
            
            # BUG: Saving checkpoint may fail due to disk space or permissions
            if epoch % 10 == 0:
                save_checkpoint(model, epoch, f"checkpoints/model_epoch_{epoch}.pt")
                
        except (OSError, PermissionError) as e:
            print(f"Runtime I/O error at epoch {epoch}: {e}")
            # Training may need to be restarted or resumed from last successful checkpoint
            raise RuntimeError(f"Training interrupted due to I/O failure: {e}")
```

**Issue**: Network instability, server downtime, or connectivity issues cause random failures when downloading pretrained models or datasets, leading to non-deterministic exceptions.

These examples demonstrate the seven main categories of crashes that can occur in deep learning systems, each with distinct characteristics and failure modes that the DaiFu benchmark aims to address.
        