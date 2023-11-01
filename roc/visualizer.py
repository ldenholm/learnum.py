import pandas as pd
import numpy as np
from matplotlib.pyplot import subplots
import matplotlib.dates as mdates
import datetime as dt

GRAPH_PATH = "/graphs"

ds = pd.read_csv('data/dandenong.csv', index_col='id')

fig, ax = subplots(figsize=(8, 8))
#ax.plot(ds['PM10'], ds['NO2'], 'o')
#fig.savefig(f'{GRAPH_PATH}/1')

#print(ds['NO2'])


# We must construct a list of the datetimes. Let's use this method:
# Sample datetime: 2022-01-01 00:00:00
dates = [date for date in ds['datetime_local']]
x = [dt.datetime.strptime(d, '%Y-%m-%d %H:%M:%S').date() for d in dates]
# assuming it's 1:1 we plot PM10 on y-axis:
y = ds['PM10']
print(x)

fig.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
fig.gca().xaxis.set_major_locator(mdates.MonthLocator())
ax.set_xlabel('Month (2022)')
ax.set_ylabel('Particulate Matter diameter of 10 micrometers')
ax.plot(x, y, 'o')
fig.savefig(f'{GRAPH_PATH}newplt2-{dt.datetime.now()}')