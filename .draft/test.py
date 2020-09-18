from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
import mplfinance as mpf
import pandas as pd

import configparser

config = configparser.ConfigParser()
config.read('../conf/properties.conf')
#for key in config['DEFAULT']: print(key)
#key = config['API-KEY']['KEY_ONE']


cc = CryptoCurrencies(key=config['API-KEY']['KEY_ONE'])
cc.output_format='pandas'
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
print(data.columns)
data.describe()

