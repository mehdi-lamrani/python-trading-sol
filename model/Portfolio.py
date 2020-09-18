from typing import Dict


class Asset:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value: str):
        self._name = value

    @property
    def price(self):
        return self._value

    @price.setter
    def price(self,value: float):
        self._price = value


class Direction:
    BUY = "BUY"
    SELL = "SELL"


class Order:

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self,value: Direction):
        self._direction = value

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self,value: Asset):
        self._asset = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value: int):
        self._quantity = value

    def value(self) -> float:
        if self.direction is Direction.BUY:
            return self._asset.price * self.quantity
        elif self.direction is Direction.SELL:
            return - self._asset.price * self.quantity

    def toStr(self):
        return " ".join([self.direction, self.asset.name, self.quantity])


class Portfolio(Dict):

    def __init__(self,name:str, balance: float):
        self.name = name
        self.balance = balance

    @property
    def assets(self):
        return self._assets

    # @assets.setter
    # def assets(self, value:List[PortfolioEntry]):
    #    self._assets = value

    def buy(self,asset: Asset,qty: int):
        order = Order(Direction.BUY,asset,qty)
        self.placeOrder(order)

    def sell(self,asset: Asset,qty: int):
        order = Order(Direction.SELL,asset,qty)
        self.placeOrder(order)

    def placeOrder(self, order:Order):
        if order.direction is Direction.BUY :
            if order.value() > self.balance:
                raise InsufficientFundsException(self,order.asset)
            if order.asset.name not in self:
                self[order.asset.name] = order.value()

        if order.direction is Direction.SELL :
            if order.asset.name not in self:
                raise AssetNotPresentException(self,order.asset)
                # raise Exception('{} asset is not part of the portfolio. \n sell operation not possible.'.format(asset.name))

        self[order.asset.name] = (self[order.asset.name] + order.value())
        self.balance = self.balance - order.value()


class AssetNotPresentException(Exception):
    """Exception raised if the asset is not present in the portfolio
    Attributes:
        portfolio -- the portfolio
        asset -- the missing asset
    """

    def __init__(self,portfolio:Portfolio,asset: Asset):
        self.asset = asset
        self.portfolio = portfolio
        self.message = '{} asset is not part of the portfolio. {}'.format(asset.name).format(portfolio.name)

        super().__init__(self.message)


class InsufficientFundsException(Exception):
    """Exception raised if the asset is not present in the portfolio
    Attributes:
        portfolio -- the portfolio
        asset -- the missing asset
    """

    def __init__(self,  portfolio:Portfolio, order:Order):
        self.portfolio = portfolio
        message = 'Portfolio {} do not have sufficient funds to perform the operation'.format(portfolio.name)
        message += '\nBalance : {}'.format(portfolio.balance)
        message += '\nOrder : {}'.format(order.toStr())

        self.message = message


        super().__init__(self.message)
