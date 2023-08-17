import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Let's render a system of linear equations:
# So essentially we create intervals of reals (floating points)
# then construct a mesh from those intervals seems to be: [a, b).
# The mesh generates coordinate matrices for the given input vector.

# Suppose we want to render a system of 3 equations in 3 unknowns.
def plotSystem(ax):
    x, y = np.linspace(1, 10, 10), np.linspace(1, 10, 10)
    X, Y = np.meshgrid(x, y)
    # Now we define our matrix:
    Z1 = 4 + X + 2*Y 
    Z2 = 0 + 2*X + 3*Y
    Z3 = 4 + 10*X + 4*Y

    # Plot the surfaces:
    ax.plot_surface(X, Y, Z1, alpha=0.5)
    ax.plot_surface(X, Y, Z2, alpha=0.5)

# Setup figure:
fig =  plt.figure()
ax = fig.add_subplot(111, projection='3d')

plotSystem(ax)
plt.show()