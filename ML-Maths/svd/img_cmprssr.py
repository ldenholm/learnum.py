import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('bird.png')
plt.imshow(img)
plt.show()
# convert to rbg
img_gray = rgb2grey(img)
plt.imshow(img_gray, cmap=plt.get_cmap('gray'))
plt.show()