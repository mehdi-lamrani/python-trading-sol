import plotly.graph_objs as go
import chart_studio.plotly as py
import plotly
import pandas as pd
import datetime
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter

def set_cols(df):
    df.columns=['open','high','low','close','volume']

ts = TimeSeries(key='Q1K6DRQN7V02YEPA', output_format='pandas')

df, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
set_cols(df)

fig = go.Figure(data=go.Ohlc(x=df.index,
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close']))


fig.show()