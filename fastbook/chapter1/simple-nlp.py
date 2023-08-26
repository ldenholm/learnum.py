from fastai.text.all import *

#dls = TextDataLoaders.from_folder(untar_data(URLs.IMDB), valid='test', bs=32)
doc(TextDataLoaders.from_folder)
#learn = text_classifier_learner(dls, AWD_LSTM, drop_mult=0.5, metrics=accuracy)
# learn.fine_tune(4, 1e-2)
# learn.predict("The film was hilarious")