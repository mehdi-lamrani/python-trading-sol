from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from matplotlib.dates import DateFormatter
import mplfinance as mpf
import pandas as pd

today = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')


def set_cols(df):
    df.columns = ['Open','High','Low','Close','Volume']
    df.index.name = 'Date'

ts = TimeSeries(key='Q1K6DRQN7V02YEPA',output_format='pandas')

pal = plt.get_cmap('Set1')
#plt.style.use('dark_background')
fig, axs = plt.subplots(2, 2)
fig.tight_layout()

i = 0
x = 0
y = 0

def plot_stock(name):
    global i,x,y
    data,meta_data = ts.get_intraday(symbol=name,interval='1min',outputsize='full')
    # data = pd.read_csv('data/sp_iday.csv',index_col=0,parse_dates=True)
    set_cols(data)
    data = data.loc[today:today]
    mpf.plot(data,type='candle',ylabel=name,mav=(3,6,9),ax=axs[x,y])
    if y :
        x = int(not x)
    y = int(not y)
    i = i + 1


plot_stock('MSFT')
plot_stock('AMZN')
plot_stock('GOOG')
plot_stock('AAPL')

plt.show()