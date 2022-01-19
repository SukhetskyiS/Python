class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч - Превышение скорости'
        else:
            return f'{self.speed} км/ч - Допустимая скорость'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч - Превышение скорости'
        else:
            return f'{self.speed} км/ч - Допустимая скорость'


class PoliceCar(Car):
    pass


a = TownCar(100, 'Черный', 'CyberTrack', False)
b = WorkCar(40, 'Белый', 'PoliceCar', True)
print(a.show_speed())
print(b.show_speed())
