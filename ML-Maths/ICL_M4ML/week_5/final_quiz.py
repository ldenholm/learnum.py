import numpy as np
from numpy import linalg as la

L = np.array([[4, 7, 1.5], [-5, -8, -0.5], [6, 6, -2]])
eval, evec = la.eig(L)
print(evec)