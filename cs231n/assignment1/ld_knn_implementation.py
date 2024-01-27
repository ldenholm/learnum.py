import os
import random
import numpy as np
from cs231n.data_utils import load_CIFAR10
from cs231n.classifiers import KNearestNeighbor
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
num_classes = len(classes)
for y, cls in enumerate(classes):
    # cls = classes[y]
    idxs = np.flatnonzero(y_train == y)
    idxs = np.random.choice(idxs, samples_per_class, replace=False)
    for i, idx in enumerate(idxs):
        plt_idx = i * num_classes + y + 1
        plt.subplot(samples_per_class, num_classes, plt_idx)
        plt.imshow(X_train[idx].astype('uint8'))
        plt.axis('off')
        if i == 0:
            plt.title(cls)
plt.show()


# Subsample data for more efficient run time during this exercise
num_training = 5000
mask = list(range(num_training))
X_train = X_train[mask]
y_train = y_train[mask]

num_test = 500
mask = list(range(num_test))
X_test = X_test[mask]
y_test = y_test[mask]

# Reshape image data into rows
X_train = np.reshape(X_train, (X_train.shape[0], -1))
X_test = np.reshape(X_test, (X_test.shape[0], -1))
print(X_train.shape, X_test.shape)

# Now we use the cs231n implementation of KNN classifier included in their lib.
classifier = KNearestNeighbor()
classifier.train(X_train, y_train)