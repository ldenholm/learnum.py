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