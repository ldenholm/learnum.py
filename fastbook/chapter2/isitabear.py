from fastai.vision.all import *
import matplotlib.pyplot as plt

path = Path('bears')
bears = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128)
    )
# (ImageBlock, CategoryBlock) = tuple describing types for independent and dependent variables.
# In this case y = f(x), where x = bear imgs, and y = classification (grizzly, black, teddy).

# Our items in this dataloder are file paths, get_items requires a function to retrieve such items.
# get_image_files will accept the path given as an argument when we instantiate our Dataloaders object.

# Splitter constructs the validation set using a random split method.

# get_y accepts a function for providing the target label (classification) for each item.
# parentlabel() returns a given filepaths parent directory. Since we downloaded our images into
# folders whose names are their respective labels we can leverage the simplicity of parentlabel().

# We need to normalize our input data so we do not train with batches of different sized images.
# To do so we perform a transformation on each item in the dataset by resizing them all to 128x128.

# Now we have successfully constructed a datablock, a blueprint for our Dataloaders.
# Next we must specify the path where our data (images) may be found:

dls = bears.dataloaders(path)

# Dataloaders (Fastai) includes a training and a validaiton Dataloader (Pytorch).
# Dataloader provides batches of multiple items to the GPU. When looping through
# Dataloader 64 items (by default) are stacked up into a single tensor and we may
# inspect these items with the following:

#dls.valid.show_batch(max_n=4, nrows=1)
#plt.show()

# We can use a different transform on each item in the batch. In this example we use
# RandomResizedCrop to illustrate the benefits of training on random crops of the items.

bears = bears.new(item_tfms=RandomResizedCrop(128, min_scale=0.3))
# Min scale controls how much of the image to capture. In this case 30%.
dls = bears.dataloaders(path)
dls.train.show_batch(max_n=4, nrows=1, unique=True)
# We set unique = true to view the same image affected by the RandomResizedCrop transform.
plt.show()


# Data Augmentation involves creating variations of the input data to better train a model.
# In our current example we data augmentation operations include rotation, stretching, warping,
# flipping, contrast & brightness changes.

# We can apply these transformations to the entire batch using GPU. Here is an example:
bears = bears.new(item_tfms=Resize(128), batch_tfms=aug_transforms(mult=2))
dls = bears.dataloaders(path)
dls.train.show_batch(max_n=8, nrows=2, unique=True)
plt.show()
# We are not using RandomResizedCrop so its easier to see the results of augmentation.