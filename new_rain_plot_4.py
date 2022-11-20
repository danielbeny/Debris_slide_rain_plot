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
fig = plt.figure()
plt.rc('font', size=4 ) 
locator = mdates.DayLocator(interval=1)
formatter = mdates.ConciseDateFormatter(locator)


plt.subplot(211)
plt.plot(temp['TIMI'], tmpr, color='black', linewidth=0.3)

plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gca().set_xlim([dt(2013,2,16),dt(2013,3,2)], auto=True)

plt.ylabel('Temperature [°C]', size=4)
plt.axvline(pd.Timestamp('2013-02-27 20:00'),color='r',linewidth=0.4)
plt.axhline(0,linewidth=0.2, color='black', linestyle=':')
plt.gca().tick_params(axis="x",direction="in")
plt.yticks(np.arange(-4, 10, step=4))

plt.subplot(212)
plt.plot(rain['dt'], ra, color='black', linestyle='dashed', linewidth=0.4)
plt.bar(rain['dt'],r, color='black')


plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(formatter)
plt.gca().set_xlim([dt(2013,2,16),dt(2013,3,2)], auto=True)
plt.gcf().autofmt_xdate()
plt.xticks(size=4)
plt.ylabel('Precipitation [mm]', size=4)
plt.xlabel('Date', size=4)
plt.axvline(pd.Timestamp('2013-02-27 20:00'),color='r',linewidth=0.4)
plt.yticks(np.arange(0, 470, step=100))
#plt.xticks(rotation=0)
fig.tight_layout(h_pad=-0.2)
fig.set_dpi(600.0)
plt.show()





