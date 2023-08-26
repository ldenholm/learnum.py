from fastai.vision.all import *

path = untar_data(URLs.PETS)
print('path loc: ', path)

def is_cat(x): return x[0].isupper()

# We set the seed to the same value each time so
# the validation set is constant.
# Assuring us changes in the results are due to updates
# in the model rather than a new validation set.
dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42,
    label_func=is_cat, item_tfms=Resize(224),
    num_workers=0)

# Create CNN using resnet arch with 34 layers and error rate
# for our measure of performance on the validation set. Note
# metric is distinct from the loss function. The loss function is
# chosen for gradient descent whereas metrics are chosen to be easy
# for humans to interpret the results. In this case we measure the error
# rate of the model successfully classifying an image.
def main():
    learn = vision_learner(dls, resnet34, metrics=error_rate)
    learn.fine_tune(1)

if __name__ == "__main__":
    main()