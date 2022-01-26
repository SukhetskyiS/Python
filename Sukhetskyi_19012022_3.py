class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.number_of_cells // rows)]) \
               + '\n' + '*' * (self.number_of_cells % rows)

    def __add__(self, other):
        return 'Сумма ячеек двух клеток: ' + str(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        return self.number_of_cells - other.number_of_cells if self.number_of_cells - other.number_of_cells > 0 \
            else 'Вычитание не возможно'

    def __mul__(self, other):
        return 'Произведение количества ячеек двух клеток: ' + str(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return 'Деление количества ячеек двух клеток: ' + str(round(self.number_of_cells / other.number_of_cells))


cell_1 = Cell(15)
print(cell_1.make_order(5))
print(cell_1.make_order(4))
cell_2 = Cell(21)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

