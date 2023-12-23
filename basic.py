# Current vers
# import sys
#
# print('System vers')
# print(sys.version)
# print(sys.version_info)
#
# # Current time
# import datetime
#
# now = datetime.datetime.now()
# print('current  time: ')
# print(now.strftime("%d-%m-%Y \n%H:%M:%S"))

# Напишите программу на Python,
# которая принимает радиус круга от пользователя и вычисляет площадь.
# from math import pi
# r = float(input('Input radius: '))

# print ('площадь круга с радиусом: ' + str(r) + ' равна ' + str(pi * r**2))

# 5. Напишите программу на Python, которая принимает имя и фамилию пользователя
# и печатает их в обратном порядке с пробелом между ними.

# name1 = input('Введите имя: ')
# name2 = input('Введите фамилию: ')
# print (name2 + ' ' + name1)

# Напишите программу на Python, которая принимает от пользователя
# последовательность чисел, разделенных запятыми, и
# генерирует список и кортеж с этими числами

# values = input('input sequence of numbers: ')
# list = values.split(',')
# tuple = tuple(list)
# print ('List is:', list)
# print ('Tuple is:', tuple)
# print('first value of list is:', list[0])
# print('first value of tuple is:', tuple[0])

# Напишите программу на Python, которая будет принимать
# имя пользователя от пользователя, и распечатайте его расширение

# value_name = input('Input name of file: ')
# f_extns = value_name.split('.')
# print('The extension of the file is '+ repr(f_extns[1]))
# print('The extension of the file is '+ (f_extns[1]))


# my_list = [1,3,5]
# my_list.append(input('input value to add '))
# print('new list is ', my_list)

# print(type(my_list[2]))

# 8. Напишите программу на Python для отображения
# первого и последнего цветов из следующего списка.

# color_list = ['red', 'green','blue']
# print('first color is ', color_list[0],'\n' 'last color is ', color_list[-1])

# 9. Напишите программу на Python для отображения расписания экзаменов. (извлеките дату из exam_st_date). Перейти к редактору
# Пример вывода: Экзамен начнется с: 11/12/2014

# exam_st_date = (11, 12, 2014)
# print('the Examination will  start from: ', exam_st_date[0],'/', exam_st_date[1], '/', exam_st_date[2])

# start_exam = (1,12,2023)
# print('%i,%i,%i' %start_exam)

# 10. Напишите программу на Python, которая принимает целое число (n) и
# вычисляет значение n + nn + nnn.

# a = int(input('Input an integer: '))
# n1 = int('%s'%a)
# n2 = int('%s%s'%(a,a))
# n3 = int('%s%s%s'%(a,a,a))
# print(n1+n2+n3)

# Напишите программу на Python для печати календаря с указанным месяцем и годом.
import calendar
from idlelib.iomenu import encoding

# actualy_date = datetime.datetime.now()
# y =int(input('Input year: '))
# m =int(input('Input month: '))

# print(calendar.month(y,m))

# Напишите программу на Python для расчета количества дней между двумя датами.
# Даты выборки : (2014, 7, 2), (2014, 7, 11)
# Ожидаемый выход : 9 дней

# from datetime import date
# f_date=date(2014,7,2)
# l_date=date(2014,7,11)
# delta = l_date-f_date
# print(delta.days)

# r = 6
# V = (4/3)πr³

# volume = 4.0/3.0*3.14*r**3
# print(volume)

# 16. Напишите программу на Python, чтобы получить разницу между заданным числом и 17,
# если число больше 17, верните двойную абсолютную разницу.


# input_value = input('input value to be compared: ')
# target_value = 17
#
#
#
# if (int(input_value) > int(target_value)):
#     print('Target input > target_value DOUBLE difference in values: ')
#     print(((int(input_value) - int(target_value)))*2)
# else:
#     print('Target input < target_value DOUBLE difference in values: ')
#     print(((int(target_value) - int(input_value)))*2)

# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
#
#
# print(difference(14))

# 17. Напишите программу на Python,
# чтобы проверить, находится ли число в пределах от 0 до 100 .

# def in_range(n):
#     if int(n) in range(0, 100):
#         print('Value in the range')
#     else:
#         print('Value is not in the range')
#
#
# print(in_range(input('Input value to found it in the range ')))
#


# 18. Напишите программу на языке Python для расчета суммы трех заданных чисел,
# если значения равны, тогда верните трижды их сумму.

# def summ(a, b, c):
#     if a == b == c:
#         sum = (a + b + c) * 3
#
#     else:
#         sum = a + b + c
#     return sum
#
#
# print(summ(2, 2, 2))

# 19. Напишите программу на Python, чтобы получить новую строку из заданной строки,
# где «Is» было добавлено вперед.
# Если заданная строка уже начинается с «Is», вернуть строку без изменений.
#
# str_1 = 'The best! '
# str_2 = 'Is '
#
# if str_1.startswith('Is '):
#     print(str_1)
# else:
#     str_1 = str_2 + str_1
#     print(str_1)
#
#
# def new_str(str):
#     if len(str) >= 2 and str[0:2] == "Is":
#         return str
#     return 'Is ' + str
#
#
# print(new_str('The Best '))
# print(new_str('Is Empty'))
# print(new_str('It dog'))

# 21. Напишите программу на Python, чтобы выяснить, является ли данное число
# (принять от пользователя)
# четным или нечетным, распечатайте соответствующее сообщение для пользователя.

# user_input = int(input("Input value: "))
# ost = 1
# if user_input % 2 != ost:
#     print(f'{user_input} -> This is an even number')
# else:
#     print(f'{user_input} -> This is an odd number')

# 22. Напишите программу на Python для подсчета числа 4
# (сколько раз встречается в списке в заданном списке

# def count_value(value=None):
#     my_list = [1, 2, 3, 4, 5, 6, 4, 8, 4, 10]
#     count = 0
#     value = int(input('Enter a number: '))
#
#     for i in my_list:
#         if i == value:
#             count += 1
#
#     print(count)
#
#
# count_value()

# #  23. Напишите программу на Python, чтобы получить n (неотрицательные целые)
# #  копии первых 2 символов данной строки.
# #  Вернуть n копий всей строки, если длина меньше 2
#
# simple_string = 'Hello World'
# print(len(simple_string))
# while len(simple_string) <= 12:
#     for char in simple_string:
#         print(char)

# day_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# profit_tuple = (100, 50, 20, 10, 5, 25, 105,100,50)
# result = zip(day_tuple, profit_tuple)
# print(tuple(result))
#
# таблица умножения
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i * j:4d}', end=' ')
#     print()


# range_1 = range(1,10)
# for i in range_1:
#     for j in range_1:
#         print(f'{i*j:3}', end=' ')
#     print()

# open_file = open(r'C:\Users\Programmer\Documents\GitHub\Urban\03_code_style 4.py', encoding='UTF8')
# for line in open_file:
#     print(line)
# open_file.close()

# 27. Напишите программу на Python, чтобы объединить все элементы списка в строку и вернуть ее.

# my_list = ['Sergeant', 'Francisco', 'Jeremy']
# my_string = ' '.join(my_list)
# print(my_string)

# def concatenate_lists(list1):
#     list1 = ' '.join(list1)
#     print(list1)
#
#
# concatenate_lists(['Sergey', 'Bob', 'Alice'])

# Напишите программу на Python, чтобы распечатать набор,
# содержащий все цвета из color_list_1, которых нет в color_list_2
# ожидаемый вывод White Black

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# # с помощью встроенной ф-ции set().difference()
# color_list_difference = set(color_list_1).difference(color_list_2)
# for color in color_list_difference:
#     print(color)
# # обычным вычитанием
# difference_value = color_list_1 - color_list_2
# for color in difference_value:
#     print(color)

# Напишите программу на Python, которая примет основание и высоту треугольника и вычислит площадь
# S = (1/2)ah
# где a - основание треугольника, h - высота, опущенная на это основание.

# def triangle_square(a=int, h=int):
#     square = (a * h)/2
#     print(square)
#
# triangle_square(1,6)
#

# # функция поиска по списку
# def search_fruit(fruit_value):
#     fruit_list = ['apple', 'banana', 'lemon', 'orange', 'pear']
#     find_fruit = False
#
#     while fruit_value != find_fruit:
#
#         if fruit_value in fruit_list:
#             find_fruit = True
#             print(f'The {fruit_value} is in list')
#             break
#         else:
#             fruit_value = input('Please enter a valid fruit: ')
#
#
# search_fruit(input('Please enter a fruit: '))


# enumerate
# def function_with_enumerate():
#     fruit_list = ["fruit", "banana", "car", "audi"]
#     for index, item in enumerate(fruit_list):
#         print(f'Item {index}: {item}')
#     dict = {}
#     for i in range(len(fruit_list)):
#         dict[i] = fruit_list[i]
#     print(dict)
#
#
# function_with_enumerate()

# list_day = ['1', 'Monday', '2', 'Tuesday', '3', 'Wednesday', '4',
#             'Thursday', '5', 'Friday', '6', 'Saturday', '7', 'Sunday']
#
# dict_day = {}
#
# for item in list_day:
#     if item.isdigit():
#         index = int(item)
#     else:
#         dict_day[index] = item
#
# print(dict_day)
# for index, item in enumerate(dict_day):
#     print(item, ':', dict_day[item])


list_day = ['1', 'Monday', '2', 'Tuesday', '3', 'Wednesday', '4',
            'Thursday', '5', 'Friday', '6', 'Saturday', '7', 'Sunday']
list2 = [999,888,876]


def print_value_of_list(a,b=None,c=None,d=None):
    print(a,b,c,d)
    # for item in list:
    #     print(item)


# print_value_of_list(list_day)
print_value_of_list(list_day)
print_value_of_list(*list_day)
