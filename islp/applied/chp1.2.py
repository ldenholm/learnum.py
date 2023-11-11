import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ISLP import load_data
import seaborn as sn

bs = load_data("Boston")
print(bs, 'shape: ', bs.shape)

# lets use a dataframe so intellisense helps
# this is simply so in vscode my autocomplete is useful
boston = pd.DataFrame(bs)
for c in boston.columns:
    print(c)

# Construct a correlation matrix to analyze the dataset.
sn.heatmap(boston.corr(), annot=True)
plt.show()

# (d) Which predictors are associated with per capita crime rate?
# accessible radial highways (moderate positive linear),
# tax (moderate positive linear), avg distance to employement
# centers (weak negative linear), median value of owner occupied
# homes (weak negative linear). There are more however these are
# the strongest.

# (e) Do any of the suburbs of Boston appear to have particularly 
# high crime rates? Tax rates? Pupil-teacher ratios? 
# Comment on the range of each predictor.

#boston['crim'].plot(kind="bar").set_title('test')
print('Top 3 suburbs for crime rate in descending order:\n', boston['crim'].nlargest(3), 
      "\nRange of crime rate in the dataset:\n", (boston['crim'].max() - boston['crim'].min()))
# The high range of crime rate in the data set implies this predictor does not represent the central tendency of the data.
print('Top 3 suburbs for tax rate in descending order:\n', boston['tax'].nlargest(3),
      "\nRange of tax rate in the dataset:\n", (boston['tax'].max() - boston['tax'].min()))
# Tax rate range similar result to the crime rate.
print('Top 3 suburbs for pupil-teacher ratio in descending order:\n', boston['ptratio'].nlargest(3),
      "\nRange of ptratio rate in the dataset:\n", (boston['ptratio'].max() - boston['ptratio'].min()))
# Pupil-teacher ratio range is relatively small which suggests its the strongest measure of central tendency out of these 3 predictors.
plt.show()

# (f) How many suburbs (rows) bound the Charles river?
print('Number of suburbs in data set which bound the Charles river: ', 
      boston.loc[boston['chas'] == 1].shape[0])

# (g) What is the median pupil-teacher ratio among the towns in this data set?
print('median pupil-teacher ratio: ',
      boston['ptratio'].median())

# todo fix this, need to get the min samples row num:
#print('finding lowest median value of owner occupied homes: ',
      #boston.index[boston['medv'].min()])