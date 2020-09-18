from abc import ABC
import datetime

class Value(ABC):
    def __init__(self, name):
        self.name = name
        self._open = 0
        self._high = 0
        self._low = 0
        self._close = 0
        self._volume = 0

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self,datetime:datetime):
        self._datetime = datetime

    @property
    def open(self):
        return self._open

    @open.setter
    def open(self, open:float):
        self._open = open

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self,high:float):
        self._high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low:float):
        self._low = low

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self,close:float):
        self._close = close

    @property
    def volume(self):
        if (self._volume is not None):
            return self._volume
        else :
            return 0


    @volume.setter
    def volume(self, volume:int):
        self._volume = volume