import numpy as np

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