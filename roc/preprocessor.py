import pandas as pd
import numpy as np

DATA_PATH = 'data'

# ds = pd.read_excel(f'{DATA_PATH}\\2022_All_sites_air_quality_hourly_avg_AIR-I-F-V-VH-O-S1-DB-M2-4-0.xlsx', sheet_name='Dandenong_10022')
# print(ds)
# ds.to_csv(f'{DATA_PATH}\\dandenong.csv')

ds = pd.read_csv(f'{DATA_PATH}\\dandenong.csv',
                 na_values='',
                 index_col='id')
print(ds)
print('PM10:\n', ds['PM10'])
print(len(np.unique(ds['PM10'])))
print(ds['PM10'].mean())
print('shape of data: ', ds.shape)

# Show all the features for the dataset:
features = ds.columns
print(features)
print('first x rows:\n', ds[:5])
# Select certain columns:
pm10_vectorwindvel = ds[['PM10', 'VWS']]
print(pm10_vectorwindvel[:5])

# We can do cool stuff like construct a boolean
# array to grab those entries having PM10 > 50, then
# use loc[] to run it against the root dataset:
print(ds.loc[lambda x: x['PM10'] > 50, ['PM10', 'datetime_AEST', 'O3']])

# Same thing but multiple conditions (note the single & is equivalent to && operator):
print('Entries with PM10 > 70, N02 > 12\n', 
      ds.loc[lambda x: (x['PM10'] > 70) & (x['NO2'] > 12), ['PM10', 'NO2', 'datetime_AEST', 'O3']])