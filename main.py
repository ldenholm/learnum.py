import torch as t
import numpy as np

t1 = t.tensor(2.)
print(t1.dtype)

vec = t.tensor([1, 2, 3])
print(vec)

linsys = t.tensor([
    [2, 4, 5],
    [ 1, 3, 5],
    [2, 2, 4]
])
print(linsys, linsys.dtype)
print('demensions of the matrix, m*n', linsys.shape)

tensor = t.tensor([
    [[1,2,3], [3,2,1], [4,3,2]],
    [[1,0,0], [0,1,0], [0,0,1]]
])
print('tensor dimensions', tensor.shape)

# todo: lookup computing gradients
print('dy/dx', t.gradient())
t.gradient