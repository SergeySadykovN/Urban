class Vehicle:
    """родительский(базовый) класс Vehicle, который имеет свойство vehicle_type"""
    vehicle_type = "None"


class Car:
    """родительский(базовый) класс Car, который имеет свойство price = 1000000"""
    price = 10000

    def horse_powers(self):
        """функция  возвращает количество лошадиных сил для автомобиля"""
        return 100


class Nissan(Vehicle, Car):
    """наследник класса Car и Vehicle - класс Nissan
    переопределите свойство price и vehicle_type,
    а также переопределите функцию horse_powers"""
    price = 2000000
    vehicle_type = "Car"

    def horse_powers(self):
        return 150


automobile1 = Nissan()
print(automobile1.vehicle_type, automobile1.price, automobile1.horse_powers())
