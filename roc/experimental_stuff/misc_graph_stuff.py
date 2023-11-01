import numpy as np
import pandas as pd
import datetime as dt

FIG_PATH = '..\\graphs'

ds = pd.read_csv('..\\data\\dandenong.csv')

ax = ds.plot.scatter('SWS', 'PM10')
ax.set_title('Scalar Wind Speed vs PM10')
fig = ax.figure
fig.savefig(f'{FIG_PATH}\\pm10-vs-sws-{dt.datetime.now().strftime("%Hhr-%Mmin-%d-%m-%y")}.png')
print(ds)