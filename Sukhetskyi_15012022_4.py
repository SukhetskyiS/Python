class Car:
    speed = 50
    color = 'Red'
    name = 'Tesla CyberTrack'
    is_police = False

    def go(self):
        return 'Поехала'

    def stop(self):
        return 'Остановилась'

    def turn(self):
        return 'Налево'

    def show_speed(self):
        return Car.speed


class TownCar(Car):
    def show_speed(self):
        if Car.speed > 60:
            return 'Превышение скорости'
        else:
            return 'Допустимая скорость'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if Car.speed > 40:
            return 'Превышение скорости'
        else:
            return 'Допустимая скорость'


class PoliceCar(Car):
    pass


a = TownCar()
b = WorkCar()
print(a.show_speed())
print(b.show_speed())
