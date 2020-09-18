import model.Value

class FXPair(model.Value):
    def __init__(self, name):
        self.name = name

    @property
    def base(self):
        return self._base

    @open.base
    def base(self, base:str):
        self._base = base


    @property
    def counter(self):
        return self._counter

    @open.setter
    def counter(self, counter:str):
        self._counter = open