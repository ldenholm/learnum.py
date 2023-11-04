import pandas as pd
import matplotlib.pyplot as plt

college = pd.read_csv('../data/College.csv')
college2 = pd.read_csv('../data/College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'},
                          axis=1)
college3 = college3.set_index('College')
college = college3
#print(college)

print(college.describe())
pd.plotting.scatter_matrix(college[['Top10perc',
                                   'Apps',
                                   'Enroll']])
plt.show(block = True)
college.boxplot(column='Outstate', by='Private')
plt.show()

# Create new qualitative var Elite from splitting the
# Top10perc var into two groups based on whether the
# proportion of students coming from the top 10% of 
# their high school classes exceeds 50%, aka the top performers.

college['Elite'] = pd.cut(college['Top10perc'],
                          [0, 0.5, 1],
                          labels=['No', 'Yes'])

print(college['Elite'].value_counts())

pd.plotting.boxplot(data=college, column='Outstate', by='Elite')
plt.show()

# Produce some histograms with varying number of bins for several quantitative
# variables of the college data set.
fig, ax = plt.subplots(nrows=2, ncols=2)
college.plot.hist(bins=4, ax=ax[0, 0])
college.plot.hist(bins=10, ax=ax[0, 1])
college.plot.hist(bins=8, ax=ax[1, 0])
college.plot.hist(bins=7, ax=ax[1, 1])
#plt.subplots(2, 2)
plt.show()

college.boxplot(column='PhD', by='Private')
plt.show()

college.boxplot(column='Room.Board', by='Private')
plt.show()

# Plot top10perc against grad rate
college.plot.scatter(x='Top10perc', y='Grad.Rate')
plt.show()

# Brief summary of the data. Key points from an early glance:
# - Private colleges have fewer phd's on average when compared
# to non private colleges.
# - Private colleges have increased room board costs compared with
# non private colleges, on average +%500 increased board cost.
# - There is a moderate positive linear correlation for colleges having
# top 10% performing students from high school and graduation rate.