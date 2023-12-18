import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2grey(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('bird.png')
#plt.imshow(img)
#plt.show()
# convert to rbg
img_gray = rgb2grey(img)
#plt.imshow(img_gray, cmap=plt.get_cmap('gray'))
#plt.show()

# Next we use truncated SVD so we can target different ranks
U, S, V = np.linalg.svd(img_gray, full_matrices=False)
print(U.shape, S.shape, V.shape)
print(U[:,1:20].shape)
# Test some different ranks
for r in [40, 80, 10]:
    #lowRankApprox = np.matmul(np.matmul(U[:1:r], np.diag(S[1:r])), V[:, 1:r])
    #plt.imshow(lowRankApprox, cmap=plt.get_cmap('gray'))
    #plt.title('rank approx of r = ' + str(r))
    #plt.show()
    A_reconstructed = U @ np.diag(S) @ V