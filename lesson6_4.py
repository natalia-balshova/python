class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, my_turn):
        self.my_turn = my_turn
        if self.my_turn == 'right':
            print(f'Машина {self.name} повернула направо')
        elif self.my_turn == 'left':
            print(f'Машина {self.name} повернула налево')
        else:
            print('Ошибка, направление указано неверно!')

    def show_speed(self):
        print(f'Cкорость {self.name} составляет: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f"Cкорость {self.name} превышена!" if self.speed > 60 else f'Cкорость {self.name} составляет: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print("Cкорость превышена!" if self.speed > 40 else f'Cкорость составляет: {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


car1 = TownCar(65, 'yellow', 'TownCar')
print(f'Машина полицейская? {car1.is_police}')
car1.show_speed()
car1.turn('left')
print()
car2 = PoliceCar(120, 'blue', 'PoliceCar')
print(f'Машина полицейская? {car2.is_police}')
car2.show_speed()
car2.turn('right')
print()
car3 = WorkCar(35, 'brown', 'WorkCar')
print(f'Машина полицейская? {car3.is_police}')
car3.stop()
car3.go()
car3.turn('left')
car3.turn('right')
car3.show_speed()
car3.speed = 50
car3.show_speed()