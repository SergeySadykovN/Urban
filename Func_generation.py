"""Задача 1: Фабрика Функций
Написать функцию, которая возвращает различные математические функции
(например, деление, умножение) в зависимости от переданных аргументов."""


def gen_func(operator):
    if operator == '+':
        def multiplier(x, y):
            return x + y

        return multiplier
    elif operator == '-':
        def multiplier(x, y):
            return x - y

        return multiplier
    elif operator == '*':
        def multiplier(x, y):
            return x * y

        return multiplier
    elif operator == '/':
        def multiplier(x, y):
            return x / y

        return multiplier
    else:
        raise Exception("Invalid operator")


operator_value = "*"
func = gen_func(operator_value)
result = func(3, 2)
print(f'result by generator: {result}')
# result by generator: 6

"""Задача 2: Лямбда-Функции
Использовать лямбда-функцию для реализации простой операции и 
написать такую же функцию с использованием def. Например, возведение числа в квадрат"""

multyply_squared = lambda x: x ** 2
result = multyply_squared(2)
print(f'result by lambda: {result}')


# result by lambda: 4


def squared_value(x):
    return x ** 2


result1 = squared_value(2)
print(f'result by def: {result1}')
# result by def: 4

"""Задача 2.1: Лямбда-Функции
Использовать лямбда-функцию перемножить список значений на х"""
list_value = [1, 2, 3, 4, 5]
result2 = map(lambda x: x * 3, list_value)
print(f'result by lamda list multiplication on 3 : {list(result2)}')
# result by lamda list multiplication on 3 : [3, 6, 9, 12, 15]

"""Задача 2.2: Лямбда-Функции
Использовать лямбда-функцию сложить два списка"""
list_value1 = [1, 2, 3, 4, 5]
list_value2 = [1, 2, 3, 4, 5]
result3 = map(lambda x, y: x + y, list_value1, list_value2)
print(f'result by lambda list addition: {list(result3)}')
# result by lambda lists addition: [2, 4, 6, 8, 10]


"""Задача 3: Вызываемые Объекты
Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, 
который возвращает площадь прямоугольника, то есть a*b."""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

    def __str__(self):
        return f'rectangular area {self.a} X {self.b} = {self.__call__()}'


# v.1
square = Rectangle(3, 2)
result4 = square()
print(f'rectangular area = {result4}')
# rectangular area = 6

# v.2
square2 = Rectangle(4, 3)
print(square2)
# rectangular area 4 X 3 = 12
