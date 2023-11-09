import pandas as pd
import numpy as np

Auto = pd.read_csv('../data/Auto.csv')
# Drop any rows containing missing values:
Auto.dropna()

# Sanitize dataset in O(n) by removing any ? values, and cast to num
Auto = Auto.replace("?", 0)
Auto['horsepower'] = pd.to_numeric(Auto['horsepower'])

print(Auto)

# Which predictors are qualitative/quantitative?
# Qualitative: {Name}
# Quantitative: {mpg,cylinders,displacement,horsepower,weight,acceleration,year,origin}

# It's breaking because we have a '?' in the horsepower col, sanitize above

print('test min and max of mpg and cyl')
print(np.max(Auto['horsepower']))
# print('hp max: ', np.max(int((Auto['horsepower']))))
# print('hp min: ', np.min(int((Auto['horsepower']))))

for column in Auto:
    # it's  gonna fail on the qualitative values
    if column == "name":
        print('breaking')
        break
    i = Auto[column]
    min, max, mean, std = np.min(i), np.max(i), np.mean(i), np.std(i)
    #min, max, mean = np.min(Auto[column]), np.max(Auto[column]), 
    range = (max - min)
    print(f'{column} min = {min} max = {max}, range = {range}, mean = {mean}, std = {std}')