import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.array([[1, 1, 2],
              [1, 2, -1],
              [1, 3, 1]])
b = np.array([1, -2, 5])
#Ax = b
x = np.linalg.solve(A, b)
print(x)

# Todo: Import matplotlib and plot.