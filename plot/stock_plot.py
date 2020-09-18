from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter

today = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

def set_cols(df):
    df.columns=['open','high','low','close','volume']

ts = TimeSeries(key='Q1K6DRQN7V02YEPA', output_format='pandas')

pal = plt.get_cmap('Set1')

fig, axs = plt.subplots(2, 2)
fig.tight_layout()


plt.subplots_adjust(  hspace=0.5)

ax = plt.subplot(2,2,1)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
set_cols(data)
data = data.loc[today:today]
plt.xticks(rotation=45)
plt.plot(data['close'], color = pal(0), linewidth=0.6, alpha=0.9)
plt.title('MSFT '+today, color = pal(0))

ax = plt.subplot(2,2,2)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
#data, meta_data = ts.get_intraday(symbol='GOOG',interval='1min', outputsize='full')
set_cols(data)
data = data.loc[today:today]
plt.xticks(rotation=45)
plt.plot(data['close'], color = pal(1), linewidth=0.6, alpha=0.9)
plt.title('GOOG '+today, color = pal(1))

ax = plt.subplot(2,2,3)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

#data, meta_data = ts.get_intraday(symbol='AMZN',interval='1min', outputsize='full')
set_cols(data)
data = data.loc[today:today]
plt.xticks(rotation=45)
plt.plot(data['close'], color = pal(2), linewidth=0.6, alpha=0.9)
plt.title('AMZN '+today, color = pal(2))

ax = plt.subplot(2,2,4)
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
#data, meta_data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize='full')
set_cols(data)
data = data.loc[today:today ]
plt.xticks(rotation=45)
plt.plot(data['close'], color = pal(3), linewidth=0.6   , alpha=0.9)
plt.title('AAPL '+today, color = pal(3))

for i,ax in enumerate(axs.flatten()):
    ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%y %H:%M'))
#plt.title('Intraday Times Series')
plt.show()