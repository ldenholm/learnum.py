import numpy as np

A = np.array([[1, 1, 2],
              [1, 2, -1],
              [1, 3, 1]])
b = np.array([1, -2, 5])
#Ax = b
x = np.linalg.solve(A, b)
print(x)