from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
import mplfinance as mpf
import pandas as pd

today = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')

def set_cols(df):
    df.columns=['Open','High','Low','Close','Volume']
    df.index.name = 'Date'


ts = TimeSeries(key='Q1K6DRQN7V02YEPA', output_format='pandas')

pal = plt.get_cmap('Set1')
plt.style.use('dark_background')

i = 0
def plot_stock(name):
    global i
    data, meta_data = ts.get_intraday(symbol=name,interval='1min', outputsize='full')
    #data = pd.read_csv('data/sp_iday.csv',index_col=0,parse_dates=True)

    set_cols(data)
    data = data.loc[today:today]
    #data = data.drop('Volume',axis=1)  # Volume is zero anyway for this intraday data set
    #data.shape
    #data.head(3)
    #data.tail(3)
    mpf.plot(data,type='candle',mav=(3,6,9),volume=True)
    i = i+1

plot_stock('MSFT')
#plot_stock('AMZN')
#plot_stock('GOOG')
#plot_stock('AAPL')

plt.style.use('dark_background')
#plt.title('Intraday Times Series')
plt.show()