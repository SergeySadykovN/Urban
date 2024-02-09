"""Дан список целых чисел, примените функции map и filter так,
чтобы в конечном списке оставить нечётные квадраты чисел"""


def number_squares(x):
    return x ** 2
    pass


def is_odd(x):
    return x % 2


list_in = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(number_squares, filter(is_odd, list_in))

print(list(result))  # [1, 25, 49, 121, 1225, 7921]
