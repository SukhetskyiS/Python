class Stationery:
    title = 'name'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Ручка'


class Pencil(Stationery):
    def draw(self):
        return 'Карандаш'


class Handle(Stationery):
    def draw(self):
        return 'Маркер'


a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())
