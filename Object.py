class Car:
    """класс Car с атрибутами конкретной машины: марка, цвет и скорость.
    + методы для увеличения и уменьшения скорости"""
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.__speed = 0  # Encapsulation
        self.max_speed = 200

    def actual_speed(self):
        return self.__speed

    def speed_up(self):
        if self.__speed < 100:
            self.__speed += 10
        else:
            print(f'Speed must not exceed 100 kilometers per hour.')
        return self

    def speed_down(self):
        self.__speed -= 10
        return self

    def stop(self):
        self.__speed = 0
        return self

    def get_speed(self):
        return f'Speed: {self.__speed} km/h'


my_car = Car("Audi", 'red')
print(f'Starts speed is {my_car.actual_speed()} km/h')

# с помощью цикла набираем скорость
for i in range(11):
    my_car.speed_up()
    print(my_car.model, my_car.color, my_car.get_speed())


class ElectricCar(Car):
    """Inheritance"""
    car_type = 'electric'
    battery = 100


car2 = ElectricCar('China Car', 'White')
car2 = car2.speed_up().speed_up().speed_up()
print(car2.model, car2.color, car2.car_type, car2.get_speed(), f'battery remain: {car2.battery}')
car2 = car2.speed_down().speed_down()
print(f'Speed {car2.model} after down: {car2.get_speed()} ')
car2 = car2.stop()
print(f'{car2.model} has stopped')

# Polimorph
print(f'_' * 20)


class Dog:
    def sound_like(self):
        return "Gav Gav!"


class Cat:
    def sound_like(self):
        return "Mew Mew!"


class Cow:
    def sound_like(self):
        return "Muuu!"


def some_animals(some):
    return some.sound_like()


dog = Dog()
cat = Cat()
cow = Cow()
# через объявленные экземпляры
print(f'\nFrom instances:')
for animal in (dog, cat, cow):
    print(some_animals(animal))
# бех экземпляров напрямую из классов
print(f'\nDirect from class:')
for animal in (Dog(), Cat(), Cow()):
    print(animal.sound_like())


class House:
    """Создайте инициализатор для класса House, который будет задавать
    атрибут этажности self.numberOfFloors = 0
    Создайте метод setNewNumberOfFloors(floors),
    который будет изменять атрибут numberOfFloors на параметр floors и
    выводить в консоль numberOfFloors"""

    def __init__(self):
        self.numberOfFloor = 0

    def setNumberOfFloor(self, floor):
        House.numberOfFloor = floor
        print(f'New number of floor is {floor}')


house = House()
house.setNumberOfFloor(5)
