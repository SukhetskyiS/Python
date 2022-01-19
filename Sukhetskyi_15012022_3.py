class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        my_dict = {'wage': wage, 'bonus': bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = my_dict


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name} {self.position}'

    def get_total_income(self):
        return f"{self._income['wage'] + self._income['bonus']}$"


a = Position('Dexter', 'Morgan', 'killer', 12000, 3000)
print(a.get_full_name())
print(a.get_total_income())
