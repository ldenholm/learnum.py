import numpy as np
from numpy import linalg as la

L = np.array([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
vals, vecs = la.eig(L)
print(vecs)
L_2 = np.array([[0.1, 0.7, 0.1, 0.1], [0.1, 0.1, 0.7, 0.1], [0.1, 0.1, 0.1, 0.7], [0.7, 0.1, 0.1, 0.1]])
vals2, vecs2 = la.eig(L_2)
print('vecs2: \n', vecs2)

L_3 = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
print('det', la.det(L_3))
eigvals3, eigvecs3 = la.eig(L_3)
print(eigvals3)
print(eigvecs3)

L_4 = np.array([[3/2, -1/2], [-1, 1/2]])
evals4, evecs4 = la.eig(L_4)
print('eig vals of 4', evals4)
print('eig vecs of 4', evecs4)