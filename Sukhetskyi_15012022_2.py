class Road:
    def calc(self, lenght, width, thickness):
        self._lenght = lenght
        self._width = width
        print(f'{(lenght * width * 25 * thickness) // (10 ** 3)} т.')


a = Road()
a.calc(20, 5000, 5)
a.calc(50, 200, 6)
a.calc(200, 5000, 3)
