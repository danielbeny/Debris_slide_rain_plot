import pandas as pd
import time 

from datetime import datetime as dt
from datetime import timedelta as td
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator


file = pd.read_csv("C:\pyhton_processing\Debris_slide_rain_plot\Skaftafell_all_data_1964-2020.csv",
 usecols=['TIMI','R'], parse_dates=['TIMI'])


rain=file.nlargest(30,'R')
rain['TIMI'] = rain['TIMI'].dt.strftime('%Y.%m.%d')

rain.sort_values(by='TIMI', inplace=True)
print(rain)



#set date as index
rain.set_index('TIMI',inplace=True)
fig, ax = plt.subplots()

rain.plot(kind='bar', ax=ax)

ax.xaxis_date()
ax.get_legend().remove()

#ax.set_title('30 max. precipitation days in Skaftafell (1964 - 2020)')
ax.set_ylabel('[mm/24h]', size=4)
ax.set_xlabel('Date', size=4)
ax.patches[rain.index.get_indexer(['2013.02.26'])[0]].set_facecolor('r')
ax.patches[rain.index.get_indexer(['2013.02.25'])[0]].set_facecolor('r')

plt.xticks(rotation=80)
#plt.margins(0.2)
plt.tick_params(labelsize = 4)
plt.grid( which='major', axis='y', color='black', linestyle='-', linewidth=0.1)
#fig.tight_layout()
plt.tight_layout()
fig.set_dpi(600.0)
plt.show()


