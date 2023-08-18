import numpy as np
import scipy.linalg as la

m = np.array([[2, 5, 1],
              [1, 1, 1]])
print(m.shape)

(P, L, U) = la.lu(m)
print('Lower:\n', L)
print('Upper:\n', U)