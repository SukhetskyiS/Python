class Road:
    def __init__(self, lenght, width, thickness):
        self._lenght = lenght
        self._width = width
        self.thickness = thickness

    def calc(self):
        return (f'{(self._lenght * self._width * 25 * self.thickness) // (10 ** 3)} т.')



a = Road(20, 5000, 5)
print(a.calc())
b = Road(15, 6000, 3)
print(b.calc())
