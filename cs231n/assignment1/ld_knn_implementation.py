import os
import random
import numpy as np
from cs231n.data_utils import load_CIFAR10
import matplotlib.pyplot as plt

# here's what we're going to do:
# create training set.
# classify every element (image) of the test set with k most similar training examples.
# cross validate value of k.
p = os.getcwd() + "\\cs231n\\datasets\\cifar-10-batches-py"
print(p)

# load cifar-10
X_train, y_train, X_test, y_test = load_CIFAR10(p)

# Test we loaded the ds correctly:
print('Training data shape: ', X_train.shape)
print('Training labels shape: ', y_train.shape)
print('Test data shape: ', X_test.shape)
print('Test labels shape: ', y_test.shape)

# Let's visualize some examples from the dataset.
# We show some examples of training images from each class
classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
samples_per_class = 7
for y, cls in enumerate(classes):
    # cls = classes[y]
    #idxs = np.flatnonzero(y_train == y)
    print(y_train == y)