import numpy as np

seq = np.linspace(0, 10, 11)
#print(seq, seq.tobytes())

seq2 = np.arange(0, 10)
print(seq2)
# zero based indexing and includes upper bound
print('hello'[2:4])

# N U M P Y  I N D E X I N G
A = np.array(np.arange(16)).reshape((4, 4))
print(A)
# Retrieve, element in row 3 col 2:
print(A[2, 1]) # shorthand is just m-1, n-1 for A having m x n dim

# Retrieve multiple rows:
print(A[[1, 2]])

# Retrieve multiple cols:
print('Multi cols:\n', A[:,[0, 2]])

# Convenience function to extract a submatrix from A
idx = np.ix_([1,3], [0,2,3])
print(A[idx])