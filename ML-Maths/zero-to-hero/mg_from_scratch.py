import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**2 - 4*x + 5

print(f(3))

xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)
plt.show()

# your classic derivative:
h = 0.000001
a = 4
print((f(a + h) - f(a))/h)