from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter

today = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')

def set_cols(df):
    df.columns=['open','high','low','close','volume']

ts = TimeSeries(key='Q1K6DRQN7V02YEPA', output_format='pandas')

pal = plt.get_cmap('Set1')
plt.style.use('dark_background')

fig, axs = plt.subplots(2, 2)
fig.tight_layout()

plt.subplots_adjust(  hspace=0.5)

i = 0
def plot_stock(name):
    global i
    ax = plt.subplot(2,2,i+1)
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    data, meta_data = ts.get_intraday(symbol=name,interval='1min', outputsize='full')
    set_cols(data)
    data = data.loc[today:today]
    plt.xticks(rotation=45)
    plt.plot(data['close'], color = pal(i), linewidth=0.6, alpha=0.9)
    plt.title(name + ' ' + today, color = pal(i))
    i = i+1

plot_stock('MSFT')
#plot_stock('AMZN')
#plot_stock('GOOG')
#plot_stock('AAPL')


for i,ax in enumerate(axs.flatten()):
    ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%y %H:%M'))
#plt.title('Intraday Times Series')
plt.show()