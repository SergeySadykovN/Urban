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

#  23. Напишите программу на Python, чтобы получить n (неотрицательные целые)
#  копии первых 2 символов данной строки.
#  Вернуть n копий всей строки, если длина меньше 2

simple_string = 'Hello World'
print(len(simple_string))
while len(simple_string) <= 12:
    for char in simple_string:
        print(char)
