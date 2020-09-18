from model import Value


class DigitalCurrency():
    def __init__(self,name):
        self.name = name

    @property
    def market(self):
        return self._localCurrency

    @market.setter
    def localCurrency(self,market):
        self._market = market

    @property
    def localCurrency(self):
        return self._localCurrency

    @localCurrency.setter
    def localCurrency(self,localCurrency:Value):
        self._localCurrency = localCurrency

    @property
    def dollar(self):
        return self._dollar

    @dollar.setter
    def dollar(self,dollar:Value):
        self._dollar = dollar