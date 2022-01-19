class TrafficLight:
    __color = 'Black'

    def running(self):
        from itertools import cycle
        from time import sleep
        colors = ['Red', 'Yellow', 'Green']
        sleep_time = [7, 2, 10]
        for color, time in zip(cycle(colors), cycle(sleep_time)):
            print(color, end='\n')
            sleep(time)


a = TrafficLight()
a.running()
# print(a._TrafficLight__color)
