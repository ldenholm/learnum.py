import pandas as pd
import numpy as np

Auto = pd.read_csv('../data/Auto.csv')
# Drop any rows containing missing values:
Auto.dropna()

# Sanitize dataset in O(n) by removing any ? values
for col in Auto:
    if col == "name":
        print('breaking')
        break
    Auto[col] = Auto[col] != "?"
    #Auto[col] = pd.to_numeric(Auto[col])

print(Auto)

# Within the dataset which predictors are qualitative/quantitative?
# Qualitative: {Name}
# Quantitative: {mpg,cylinders,displacement,horsepower,weight,acceleration,year,origin}

# It's breaking because we have a '?' in the horsepower col

for column in Auto:
    # it's  gonna fail on the qualitative values
    if column == "name":
        print('breaking')
        break
    # show range of each quantitative var:
    #print(column, 'range: ', 
    #      (float(Auto[column].max()) - float(Auto[column].min())))
    print('entire auto max: ', Auto.max()) # <-- this is returning a boolean, probably treating the values as strings
    print(column, 'mean: ', Auto[column].mean())