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

# We can reshape stuff:
reshape_A = np.reshape(A, (3, 2))
print('reshaped A: \n', reshape_A)

# Access A[i,j], A[0,0] = top left element
print(reshape_A[0, 0])

# Row access w/ zero based indexing
print(reshape_A[1])

# Transposes
print('A and its transpose\n', A, '\n', A.T)

# Take sqrt() of entries of A
print(np.sqrt(A)), print(A**0.5)

# Take square of entries of A
print(np.square(A)), print(A**2)

# Using np random to generate 50 independent random vars
Y = np.random.normal(size=50)
print(Y)

y = Y + np.random.normal(loc=50, scale=1, size=50)

print('y:\n', y)

print('correlation coefficient matrix\n', np.corrcoef(Y, y))


# Setting up a random seed so we keep a constant result:
# w/o seed
print(np.random.normal(scale=5, size=2))
print(np.random.normal(scale=5, size=2))

# w/ seed
rng = np.random.default_rng(270)
print(rng.normal(scale=5, size=2))
rng2 = np.random.default_rng(270)
print(rng2.normal(scale=5, size=2))

# Various other important funcs
x1 = rng.normal(2, 2, 20)
print('x1:\n', x1, '\nmean: ', x1.mean())
print('variance is std squared so:\nstd= ', x1.std(), '\nvar= ', x1.var(), '\nstdsq= ', (x1.std()**2))

v = sum(((x - x1.mean())**2 for x in x1)) / len(x1) # <-- this is why python is so sick
print('continued:\nvariance= ', v)