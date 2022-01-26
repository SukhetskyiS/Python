class Matrix:
    def __init__(self, list):
        self.list = list
        self.str = ''

    def __str__(self):
        for i in self.list:
            for x in i:
                if i.index(x) < len(i) - 1:
                    self.str += f'{x} '
                else:
                    self.str += f'{x}\n'
        return f'{self.str}'

    def __add__(self, other):
        self.str2 = ''
        if len(self.list) == len(other):
            for i, n in zip(self.list, other):
                if len(i) == len(n):
                    for x, y in zip(i, n):
                        z = x + y
                        if i.index(x) < len(i) - 1:
                            self.str2 += f'{z} '
                        else:
                            self.str2 += f'{z}\n'
                else:
                    self.str2 = 'ERROR'
        else:
            self.str2 = 'ERROR'
        return f'{self.str2}'


# a = Matrix([[1, 2, 5, 32], [1, 9, 5, 2], [0, 8, 3, 0]])
# print(a)
#
# b = [[9, 8, 8, 10], [1, 5, 8, 10], [2, 7, 10, 10, 9]]
# a + b
# print(a.str2)
#
# c = [[9, 8, 8, 10], [1, 5, 8, 10], [2, 7, 10, 10]]
# a + c
# print(a.str2)
