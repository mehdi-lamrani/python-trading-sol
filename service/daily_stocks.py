from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
import pandas as pd
from matplotlib.dates import DateFormatter
import mplfinance as mpf
from pandas import DataFrame

from conf.ConfigManager import ConfigManager


class StockService:

    def __init__(self):
        self.today = (datetime.today() - timedelta(days=3)).strftime('%Y-%m-%d')
        api_key = ConfigManager.getAPIKey()
        self.ts = TimeSeries(key=api_key,output_format='pandas')

    @staticmethod
    def prep(df: DataFrame) -> DataFrame:
        df.columns = ['Open','High','Low','Close','Volume']
        df.index = df.index.date
        df.index.name = 'Date'
        return df

    def getDaily(self,stock: str) -> DataFrame:
        data,meta_data = self.ts.get_daily(symbol=stock,outputsize='full')
        return StockService.prep(data)
