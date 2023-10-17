import numpy as np

x, y = np.array([4, 5, 7]), np.array([2, 3, 4])

print(x, y)

# vector addition
print(x + y)

# R^2x2 matrix
X = np.array([[1, 2], [3, 4]])
print(X)

# Dimensions of X
print(X.ndim)

A = np.array([[1, 2, 3], [4, 5, 6]])
# 2x3 shape of A
print(A.shape, A.dtype)
print(A.sum())