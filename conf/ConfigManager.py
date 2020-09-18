from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
import mplfinance as mpf
import pandas as pd

import configparser

class ConfigManager:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ConfigManager.__instance == None:
            ConfigManager()
        return ConfigManager.__instance

    def __init__(self):
        ConfigManager.__instance = self
        self.config = configparser.ConfigParser()
        self.config.read('/Users/saxen/PyVantage/conf/properties.conf')

    @staticmethod
    def getAPIKey() ->str:
     return ConfigManager.getInstance().config['API-KEY']['KEY_ONE']