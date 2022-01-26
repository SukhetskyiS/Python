from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def coat(self, v):
        pass

    @abstractmethod
    def costume(self, h):
        pass


class Clothes(MyAbsClass):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        if self._name.isalpha():
            return self._name
        else:
            raise Warning(f'"{self._name}" - название должно состоять только из букв')

    def coat(self, v):
        self.v = v
        return f'Для {self.name} с размером {self.v} необходимо {(self.v / 6.5 + 0.5):.2f} м ткани'

    def costume(self, h):
        self.h = h
        return f'Для {self.name} с ростом {self.h} необходимо {2 * self.h + 0.3} м ткани'


# a = Clothes('Пальто')
# print(a.coat(38))
# b = Clothes('Костюм')
# print(b.costume(185))
#
# c = Clothes('property')
# print(c.name)
#
# d = Clothes('32property')
# print(d.coat(42))
