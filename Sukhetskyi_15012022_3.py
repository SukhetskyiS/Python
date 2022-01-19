class Worker:
    my_dict = {'wage': 5000, 'bonus': 3000}
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'driver'
    _income = my_dict


class Position(Worker):
    def get_full_name(self):
        return f'{super().surname} {super().name}'

    def get_total_income(self):
        return super()._income['wage'] + super()._income['bonus']


a = Position()
print(a.get_full_name())
print(a.get_total_income())
