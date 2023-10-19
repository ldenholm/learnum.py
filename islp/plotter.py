import numpy as np
from matplotlib.pyplot import subplots

fig, ax = subplots(figsize=(8,8))
rng = np.random.default_rng(170)

x = rng.standard_normal(100)
y = rng.standard_normal(100)

ax.plot(x, y)
fig.show()

# todo: fix plot displaying