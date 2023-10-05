from fastai.vision.all import *
import matplotlib.pyplot as plt
import numpy as np
import torch as t


if __name__ == "__main__":
    matplotlib.rc('image', cmap='Greys')
    # Grab some samples from MNIST
    path = untar_data(URLs.MNIST_SAMPLE)
    print(path)
    Path.BASE_PATH = path
    #print(path.ls())

    threes = (path/'train'/'3').ls().sorted()
    sevens = (path/'train'/'7').ls().sorted()
    
    im3_path = threes[1]
    im3 = Image.open(im3_path)
    #im3.show()

    # Let's show the pixel matrix representation of the image:
    print(array(im3)[4:10,4:10])
    # Note: the slicing [x,y] on the RHS means take rows (and cols) from index 4 (included)
    # to index 10 (not included).
    # Same thing but using a Pytorch tensor:
    print(tensor(im3)[4:10,4:10])
    # Construct a colour coded gradient matrix representing the top section of the image with Pandas Data Frame
    # to get an idea of how the image is created from pixel values:
    im3_tensor = tensor(im3)
    #df = pd.DataFrame(im3_tensor[4:15,4:22])
    #df.style.set_properties(**{'font-size':'6pt'}).background_gradient('Greys')

    # One method to begin with is calculating the average pixel value for 
    # a 3 image and then for a 7. This will give us an idea of the 'ideal' pixel
    # average for a 3 & 7.

    seven_tensors = [tensor(Image.open(o)) for o in sevens]
    three_tensors = [tensor(Image.open(o)) for o in threes]
    len(three_tensors), len(seven_tensors)

    stacked_sevens = torch.stack(seven_tensors).float()/255
    stacked_threes = torch.stack(three_tensors).float()/255
    print(stacked_threes.shape)
    print('stacked three tensor rank: ', stacked_threes.ndim)

    # Calculate the mean of the 0th dimension of the rank3 tensors:
    mean3 = stacked_threes.mean(0)
    show_image(mean3)