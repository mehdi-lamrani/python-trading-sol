from typing import List
from datetime import date

from model.Value import Value


class Series(List[Value]):
    def __init__(self):
        pass

    def printme(self):
        for x in range(len(self)):
            print(self[x].datetime)
            print(self[x].open)
            print(self[x].high)
            print(self[x].low)
            print(self[x].close)
            print(self[x].volume)

    def saveToCsv(self):
        pass

    def saveToDB(self):
        pass

series = Series()

value = Value("MSFT")
value.datetime= date.today()
value.open = 1.0
value.high = 1.0
value.low = 1.0
value.close = 1.0
value.volume = 1.0



series.append(value)

value = Value("AAPL")
value.datetime= date.today()

series.append(value)

series.printme()



