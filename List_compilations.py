"""Дан список целых чисел, примените функции map и filter так,
чтобы в конечном списке оставить нечётные квадраты чисел"""


def number_squares(x):
    return x ** 2
    pass


def is_odd(x):
    return x % 2


list_in = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# применить обе функции, вывести только нечетные квадраты чисел
result = map(number_squares, filter(is_odd, list_in))
print(list(result))  # [1, 25, 49, 121, 1225, 7921]

# применить number_square ко всему списку и вывести список квадратов чисел
squared_num = [number_squares(num) for num in list_in]
print(list(squared_num))  # [1, 4, 25, 49, 144, 121, 1225, 16, 7921, 100]

# применить is_odd ко всему списку и вывести список только четных
even_num = [num for num in list_in if not is_odd(num)]
print(list(even_num))  # [2, 12, 4, 10]

# применить обе функции, вывести только четные квадраты чисел
odd_squared_num = [number_squares(num) for num in list_in if not is_odd(num)]
print(list(odd_squared_num))  # [4, 144, 16, 100]

# применить is_odd ко всему списку и вывести список только нечетных
odd_num = filter(is_odd, list_in)
print(list(odd_num))  # [1, 5, 7, 11, 35, 89]
print(odd_num)  # <filter object at 0x01B01370>




