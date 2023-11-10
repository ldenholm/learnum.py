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