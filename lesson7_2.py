from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def total_consumption(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, size, n):
        self.size = size
        self.number = n

    @property
    def total_consumption(self):
        result = (self.size / 6.5 + 0.5) * self.number
        return round(result, 2)

    def __str__(self):
        return f'На пошив пальто в количестве {self.number} затрачено {self.total_consumption} кв. м. ткани'


class Suit(Clothes):
    def __init__(self, height, n):
        self.height = height
        self.number = n

    @property
    def total_consumption(self):
        result = (2 * self.height + 0.3) * self.number
        return round(result, 2)

    def __str__(self):
        return f'На пошив костюмов в количестве {self.number} затрачено {self.total_consumption} кв. м. ткани'


c = Coat(44, 10)
print(c)
s = Suit(180, 10)
print(s)
print(f'Всего на пошив изделий затрачено {c.total_consumption + s.total_consumption} кв. м. ткани')
