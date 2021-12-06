from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def total(self):
        pass

    def __add__(self, other):
        return self.total + other.total


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def total(self):
        return round(self.v / 6.5 + 0.5)


class Costum(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def total(self):
        return round(self.h / 100 * 2 + 0.3)


coat = Coat(56)
costum = Costum(180)

print(f'{coat + costum}')