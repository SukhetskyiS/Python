class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title} - запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Ручка пишет'


class Pencil(Stationery):
    def draw(self):
        return 'Карандаш чертит'


class Handle(Stationery):
    def draw(self):
        return 'Маркер рисует'


a = Stationery('Кисточка')
b = Pen('Ручка')
c = Pencil('Карандаш')
d = Handle('Маркер')
print(a.draw())
print(b.draw())
print(c.draw())
print(d.draw())
