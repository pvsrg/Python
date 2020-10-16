class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f" turn to {direction}")

    def show_speed(self):
        print(f"текущую скорость автомобиля {self.speed:10.2f}")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"текущую скорость автомобиля {self.speed:10.2f} превышает максимальную скорость 60 км/ч")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"текущую скорость автомобиля {self.speed:10.2f} превышает максимальную скорость 40 км/ч")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(100, "White", "Pego")
car_1.go()
car_1.turn("right")
car_1.stop()
car_1.show_speed()

car_2 = WorkCar(50, "Black", "MAZ")
car_2.show_speed()

car_3 = SportCar(400, "Red", "Mazeratty")
car_3.show_speed()

car_4 = PoliceCar(180, "White", "Lada")
car_4.show_speed()
