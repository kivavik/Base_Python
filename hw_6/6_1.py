from time import sleep


class TrafficLight:
    __color = 'Цвет'

    def running(self):
        while True:
            print(f'Красный свет')
            sleep(7)
            print('Жёлтый свет')
            sleep(2)
            print('Зеленый свет')
            sleep(5)
            print('Жёлтый свет')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()
