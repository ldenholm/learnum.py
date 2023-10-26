import pandas as pd

Auto = pd.read_csv('data\\Auto.csv')
AAuto = pd.read_csv('data\\Auto.data', delim_whitespace=True)
print(Auto)
print(AAuto)