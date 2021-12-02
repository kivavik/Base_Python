from random import choice

class Car:

    direction = ['North', 'West', 'South', 'East']

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Car: {name} {color} color, police {is_police}')

    def go(self):
        print(f'{self.name}: Go')

    def stop(self):
        print(f'{self.name}: Stop')

    def turn(self):
        print(f'{self.name}: Turn {choice(self.direction)}')

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}'

class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()

class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()

class SportCar(Car):

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}. Dumib!' if self.speed < 150 else super().show_speed()

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police=True)


town_car = TownCar('"Mini"', "red", 50)
sport_car = SportCar('"Lada"', "green", 120)
work_car = WorkCar('"Gazel"', "white", 35)
police_car = PoliceCar('"Ford"', "striped", 150)

list_of_cars = [town_car, sport_car, work_car, police_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
