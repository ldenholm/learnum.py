import numpy as np

# Construct a 3x5 matrix X of random values
X = np.random.rand(3, 5)
print(X.shape, X)
# Perform svd on X
U, S, V = np.linalg.svd(X, full_matrices=True)
print('Full SVD: ', U.shape, S.shape, V.shape)
# We add padding to S because rows > cols
# Perform economy svd on X
Uhat, Shat, Vhat = np.linalg.svd(X, full_matrices=False)
print('Eco SVD: ', Uhat.shape, Shat.shape, Vhat.shape)