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

# Let's make a matrix:
#x, y = np.linspace(1, 10, 100), np.linspace(1, 10, 100)
#mesh = np.meshgrid(x, y)
#print(mesh)

# To render plot:
plt.show()