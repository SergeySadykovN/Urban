class Car:
    """родительский(базовый) класс Car, который имеет свойство price = 1000000 """
    price = 1000000

    def __init__(self, name):
        self.name = name

    def horse_powers(self):
        """функция def horse_powers,
        которая возвращает количество лошадиных сил для автомобиля"""
        return 100

    def __str__(self):
        return 'Car {}, Price: {}, Horse power: {}'.format(self.name, self.price, self.horse_powers())


class Nissan(Car):
    """наследник класса Car - класс Nissan и переопределите свойство price"""
    price = 2000000

    def __init__(self):
        Car.__init__(self, 'Nissan')

    def horse_powers(self):
        """а также переопределите функцию horse_powers"""
        return 150


class Kia(Car):
    """наследник класса Car - класс Kia и переопределите свойство price"""
    price = 3000000

    def __init__(self):
        Car.__init__(self, 'Kia')

    def horse_powers(self):
        """а также переопределите функцию horse_powers"""
        return 180


auto_2 = Nissan()
auto_3 = Kia()

print(auto_2)
print(auto_3)
