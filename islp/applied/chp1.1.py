import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

Auto = pd.read_csv('../data/Auto.csv')
# Drop any rows containing missing values:
Auto.dropna()
print('auto initial shape: ', Auto.shape)
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
    range = (max - min)
    print(f'{column} min = {min} max = {max}, range = {range}, mean = {mean}, std = {std}')

# (d) Next remove the 10th - 85th observations
auto_subset = Auto.drop(Auto.index[9:84])
print(auto_subset.shape)
print('\n-------------------------Subset of original dataset, samples 10-85 removed-------------------------\n')
for column in auto_subset:
    if column == "name":
        print('breaking')
        break
    i = auto_subset[column]
    min, max, mean, std = np.min(i), np.max(i), np.mean(i), np.std(i)
    range = (max - min)
    print(f'{column} min = {min} max = {max}, range = {range}, mean = {mean}, std = {std}')

# (e) Explore the full data set graphically

#Auto.plot.scatter(x='weight', y='year') # sort of useless
Auto.plot.scatter(x='horsepower', y='mpg')
# there is a weak negative linear correlation between horsepower and miles per gallon

Auto.boxplot(column='acceleration', by='cylinders')
# Above describes how the acceleration of the vehicles with varying cylinder sizes
# is distributed 
plt.show()

# (f) Suppose we wish to predict mpg, which other variables might be useful
# in predicting mpg?

# Let's plot some mpg versus x graphs.
figure, axis = plt.subplots(1, 2)
axis[0].scatter(Auto['year'], Auto['mpg'])
axis[0].set_title("mpg vs year")
# There is a weak positive linear correlation between year and mpg
# suggesting year can be used to predict mpg, higher year => higher mpg.
# From earlier graphs we know there is a weak neg correlation between
# horsepower and mpg which may be used to predict mpg values.
axis[1].scatter(Auto['weight'], Auto['mpg'])
axis[1].set_title("mpg vs weight")
# There is a strong negative linear correlation between weight and mpg,
# we may predict mpg from the weight of the vehicle.
plt.show()


corr = Auto.drop(columns=['name']).corr()
sb.heatmap(corr, annot=True)
plt.show()