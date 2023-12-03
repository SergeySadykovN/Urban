# Current vers
import sys

print('System vers')
print(sys.version)
print(sys.version_info)

# Current time
import datetime

now = datetime.datetime.now()
print('current  time: ')
print(now.strftime("%d-%m-%Y \n%H:%M:%S"))

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

r = 6
#V = (4/3)πr³

volume = 4.0/3.0*3.14*r**3
print(volume)