import numpy as np
import scipy.linalg as la

K = np.array([[2, -1, 0, 0, 0, 0],
              [-1, 2, -1, 0, 0, 0],
              [0, -1, 2, -1, 0, 0],
              [0, 0, -1, 2, -1, 0],
              [0, 0, 0, -1, 2, -1],
              [0, 0, 0, 0, -1, 2]])
print(K.shape)


# Identity for 6x6
I = np.identity(6)
IK = np.matmul(I, K)
print("IK:\n", IK)
# Test commutativity
KI = np.matmul(K, I)
print("KI:\n", KI)

# Decompose K = LU
P, L, U = la.lu(K)
print("Upper triangular of K:\n", U)
print("Lower triangular of K:\n", L)

# Question asks us to find a formula for constructing the
# i,jth entry of L^-1. Note E^-1 = L and L^-1 = E.

# We have L so let's compute it's inverse:
E = np.linalg.inv(L)
print('E:\n', E)