import numpy as np
from matplotlib.pyplot import subplots

fig, ax = subplots(figsize=(8,8))
y = x = np.linspace(-np.pi, np.pi, 50)
# note this the outer product, a_ij = x*(y.T)
f = np.multiply.outer(np.cos(y), 1 / (1 + x**2))
#ax.contour(x, y, f, levels=45)
#fig.show()

# lastly we show using a heatmap in which the z values
# produce increasingly red colours.

ax.imshow(f)
fig.show()