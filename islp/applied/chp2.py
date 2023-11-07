import pandas as pd

college = pd.read_csv('..\\data\\College.csv')
print(college['Private'])

college2 = pd.read_csv('College.csv', index_col=0)
college3 = college.rename({'Unnamed: 0': 'College'},axis=1)
college3 = college3.set_index('College')