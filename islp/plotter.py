import numpy as np
from matplotlib.pyplot import subplots

fig, ax = subplots(nrows=2, 
                   ncols=3,
                   figsize=(15,5))
rng = np.random.default_rng(170)

x = rng.standard_normal(100)
y = rng.standard_normal(100)

ax[0,1].plot(x, y, 'o')
ax[1,2].scatter(x, y, marker='+')

# We use the following properties of ax to set labels
# ax.scatter(x, y, marker='o')
# ax.set_xlabel("This is the x axis")
# ax.set_ylabel("This is the y axis")
# ax.set_title("Plot X vs Y")

#ax.plot(x, y, 'o')

#fig.set_size_inches(12, 3)
fig.show()
# run as python -i /path/to/script