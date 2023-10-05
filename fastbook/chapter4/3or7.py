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

    # Same for 7's:
    mean7 = stacked_sevens.mean(0)
    show_image(mean3)

    # mean3 represents an ideal 3, that is to say it is the mean numerical value of shading
    # that occurs for all 3's in our dataset.

    # We'll now use L1 and L2 norms to calculate distance from some '3' we are iterating over 
    # let's call this i and the ideal mean3.

    # Let's grab our i:
    some_3 = stacked_threes[1]

    l1norm_3 = (some_3 - mean3).abs().mean()
    l2norm_3 = ((some_3 - mean3)**2).mean().sqrt()
    print('l1 norm = ', l1norm_3, 'l2 norm = ', l2norm_3)

    # Computing L1 & L2 norms for 7s:
    l1norm_7 = (some_3 - mean7).abs().mean()
    l2norm_7 = ((some_3 - mean7)**2).mean().sqrt()
    print('l1 norm = ', l1norm_7, 'l2 norm = ', l2norm_7)

    #l1 norm =  tensor(0.1114) l2 norm =  tensor(0.2021)
    #l1 norm =  tensor(0.1586) l2 norm =  tensor(0.3021)

    # We can see from the output that the distance between some 3 and the mean3 is always
    # less than some 3 and mean7, which we will reason implies mean3 approximately
    # represents a typical 3 image and therefore an image with a low distance from mean3
    # may be classified as a 3.

    # PyTorch includes both these norms as loss functions, and Fastai exposes them in 
    # the namespace F. Note the l1 norm loss function has a 1/n coefficient to compute
    # the mean otherwise it would not be the mean absolute value (MAE). Same goes for
    # MSE which is just the Euclidean norm with a 1/n multiplier in front.

    (x,y) = F.l1_loss(some_3.float(), mean7), F.mse_loss(some_3, mean7)
    print('L1 norm aka mean absolute value', x, 'Mean Squared Error', y)

    # Tricks with tensors and array (since they are optimized in C for the GPU):

    data = [[2, 4, 6], [8, 10, 12]]
    arr = array(data)
    tns = tensor(data)

    print(arr, tns)

    # Second column of tensor:
    print(tns[1])

    # Use slicing syntax to select rows/cols [start:end]
    tns[1,1:3]

    # Add 1 to each element:
    print(tns+1)

    # Scale by half:
    print(tns*0.5)

    # Create tensors using the validation samples which will be used to measure
    # the accuracy of this classifier.

    valid3_tensor = torch.stack([tensor(Image.open(o)) for o in (path/'valid'/'3').ls()])
    valid3_tensor = valid3_tensor.float()/255

    valid7_tensor = torch.stack([tensor(Image.open(o)) for o in (path/'valid'/'7').ls()])
    valid7_tensor = valid7_tensor.float()/255

    print(valid3_tensor.shape,valid7_tensor.shape)


    # Define a function which takes two images a,b -> returning a distance between them:

    def distance(a, b: Tensor):
        return (a-b).abs().mean((-1, -2))
    
    print(distance(some_3, mean3))