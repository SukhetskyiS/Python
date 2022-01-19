from itertools import cycle
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self):
        sleep_time = [7, 2, 10]
        for color, time in zip(cycle(self.__color), cycle(sleep_time)):
            print(color, end='\n')
            sleep(time)


a = TrafficLight()
a.running()
# print(a._TrafficLight__color)
