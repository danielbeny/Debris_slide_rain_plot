import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib import pyplot
import plotly.graph_objects as go

#read temperature data and store as variables
headers = ['id','TIMI','T','D','F','FG']
temp = pd.read_csv('C:\\pyhton_processing\\Debris_slide_rain_plot\\temp1702-0103.csv'
,names = headers, usecols=['TIMI','T'], parse_dates=['TIMI'], dayfirst=True)
temp.info()

ttemp = temp['TIMI']
tmpr = temp['T']

#read rain data and store as variables
headers2 = ['id','dt','R','RA']
rain = pd.read_csv('C:\\pyhton_processing\\Debris_slide_rain_plot\\rain1702-0103.csv',names = headers2,usecols=['dt','R','RA'], parse_dates=['dt'], dayfirst=True)

r = rain['R']
ra = rain['RA']
rain.info()


#figure plotting
fig, ax1 = plt.subplots()

locator = mdates.DayLocator(interval=1)
formatter = mdates.ConciseDateFormatter(locator)

#temp line plot
ax1.plot(temp['TIMI'], tmpr, color='black')

# axis formatting
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax1.set_xlim([dt(2013,2,16),dt(2013,3,2)], auto=True)
ax1.yaxis.tick_right()
ax1.set_ylabel('Temperature [°C]')
ax1.set_xlabel('Date')

#twin X
ax2 = ax1.twinx()

#rain accumulation line plot
ax2.plot(rain['dt'], ra, color='purple')
#rain mm/24h bar chart
ax2.bar(rain['dt'],r, color='blue')

# axis formatting
ax2.xaxis.set_major_locator(locator)
ax2.xaxis.set_major_formatter(formatter)
ax2.set_xlim([dt(2013,2,16),dt(2013,3,2)], auto=True)
ax2.axvline(pd.Timestamp('2013-02-27 20:00'),color='r')
ax2.set_ylabel('Precipitation [mm]', color='blue')
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')


fig.tight_layout()
plt.show()





