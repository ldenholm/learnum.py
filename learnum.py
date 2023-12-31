import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup figure:
fig =  plt.figure()
ax = fig.add_subplot(111, projection='3d')


def parabola(x, y):
    return x**2 +y**2

def inverse_prabola(x, y):
    return -1*(x**2 + y**2) - 100

# Matplotlib needs a meshgrid to plot the functions
x, y = np.arange(-25, 25, 1), np.arange(-25, 25, 1)
X, Y = np.meshgrid(x, y)

# Z = f(x,y)
Z = parabola(X, Y)
ZZ = inverse_prabola(X, Y)

print('x and y lists', x, y)
print('X mesh', X)

ax.plot_surface(X, Y, Z, alpha=0.5)
ax.plot_surface(X, Y, ZZ, alpha=0.5)

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

plotSystem(ax)

# To render plot:
plt.show()