# class Car:
#     """класс Car с атрибутами конкретной машины: марка, цвет и скорость.
#     + методы для увеличения и уменьшения скорости"""
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#         self.__speed = 0  # Encapsulation
#         self.max_speed = 200
#
#     def actual_speed(self):
#         return self.__speed
#
#     def speed_up(self):
#         if self.__speed < 100:
#             self.__speed += 10
#         else:
#             print(f'Speed must not exceed 100 kilometers per hour.')
#         return self
#
#     def speed_down(self):
#         self.__speed -= 10
#         return self
#
#     def stop(self):
#         self.__speed = 0
#         return self
#
#     def get_speed(self):
#         return f'Speed: {self.__speed} km/h'
#
#
# my_car = Car("Audi", 'red')
# print(f'Starts speed is {my_car.actual_speed()} km/h')
#
# # с помощью цикла набираем скорость
# for i in range(11):
#     my_car.speed_up()
#     print(my_car.model, my_car.color, my_car.get_speed())
#
#
# class ElectricCar(Car):
#     """Inheritance"""
#     car_type = 'electric'
#     battery = 100
#
#
# car2 = ElectricCar('China Car', 'White')
# car2 = car2.speed_up().speed_up().speed_up()
# print(car2.model, car2.color, car2.car_type, car2.get_speed(), f'battery remain: {car2.battery}')
# car2 = car2.speed_down().speed_down()
# print(f'Speed {car2.model} after down: {car2.get_speed()} ')
# car2 = car2.stop()
# print(f'{car2.model} has stopped')
#
# # Polimorph
# print(f'_' * 20)
#
#
# class Dog:
#     def sound_like(self):
#         return "Gav Gav!"
#
#
# class Cat:
#     def sound_like(self):
#         return "Mew Mew!"
#
#
# class Cow:
#     def sound_like(self):
#         return "Muuu!"
#
#
# def some_animals(some):
#     return some.sound_like()
#
#
# dog = Dog()
# cat = Cat()
# cow = Cow()
# # через объявленные экземпляры
# print(f'\nFrom instances:')
# for animal in (dog, cat, cow):
#     print(some_animals(animal))
# # бех экземпляров напрямую из классов
# print(f'\nDirect from class:')
# for animal in (Dog(), Cat(), Cow()):
#     print(animal.sound_like())
#
#
# class House:
#     """Создайте инициализатор для класса House, который будет задавать
#     атрибут этажности self.numberOfFloors = 0
#     Создайте метод setNewNumberOfFloors(floors),
#     который будет изменять атрибут numberOfFloors на параметр floors и
#     выводить в консоль numberOfFloors"""
#
#     def __init__(self):
#         self.numberOfFloor = 0
#
#     def setNumberOfFloor(self, floor):
#         House.numberOfFloor = floor
#         print(f'New number of floor is {floor}')
#
#
# house = House()
# house.setNumberOfFloor(5)


# class Building:
#     def __init__(self, numberOfFloors, buildingType):
#         self.numberOfFloors = int(numberOfFloors)
#         self.buildingType = str(buildingType)
#
#     def __eq__(self, other):
#         return self.numberOfFloors != other
#
#
# firstBuilding = Building(10, 'simple building')
# secondBuilding = Building(100, 'skyscraper')
# thirdBuilding = Building(10, 'simple building')
# fourthBuilding = Building(10, 'not simple building')
#
# if Building.__eq__(firstBuilding, thirdBuilding):
#     print('identical')
# else:
#     print('not identical!')
#
# # if firstBuilding == thirdBuilding:
# #     print('equal')
# # else:
# #     print('not equal!')


# class Building:
#     '''Создайте новый класс Building с атрибутом total
#     Создайте инициализатор для класса Building, который будет
#     увеличивать атрибут количества созданных объектов класса Building total
#     В цикле создайте 40 объектов класса Building и выведите их на экран командой print'''
#     total = 0
#
#     def __init__(self):
#         Building.total += 1
#
#     def __str__(self):
#         return str(f'new building of the city, total buildings: {Building.total}')
#
#
# city = []
#
# for i in range(5):
#     building = Building()
#     city.append(building)
#     print(Building.__str__(''))

# class Summ:
#     def __init__(self, value):
#         self.sum = value
#
#     def __add__(self, other):
#         return Summ(self.sum + other.sum)
#
#     def __sub__(self, other):
#         return Summ(self.sum - other.sum)
#
#     def __str__(self):
#         return str(self.sum)
#
#     def __ne__(self, other):
#         return self.sum != other.sum
#
#     def __eq__(self, other):
#         return self.sum == other.sum
#
# value1 = Summ(2)
# value2 = Summ(3)
#
# # print((value1+value2))
# print(Summ.__sub__(value1, value2))
# # print(Summ.__ne__(value1, value2))
# # print(value2!=value1)
# # print(Summ.__eq__(value1, value2))

#

# class String:
#     def __init__(self, text):
#         self.text = text
#
#     def __rsub__(self, other):
#         return self.text
#
#     def __str__(self):
#         return self.text
#
#
#
# str1 = String("Hello World")
# str2 = String("Hello")
# result = str1 - str2
#
# print(result.__str__)

