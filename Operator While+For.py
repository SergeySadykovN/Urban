# ## Тренирую While For
#
# # # Цикл по числам Фибоначи fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
# #
# # f1 = 1
# # f2 = 1
# # print(f1)
# # while f2 < 100:
# #     print(f2)
# #     next_f2 = f1 + f2
# #     next_f1 = f2
# #     f1 = next_f1
# #     f2 = next_f2
#
# #Создайте список из 5 машин
# # Создайте цикл for и в цикле распечатайте
# # каждый из автомобилей в строке 'Я езжу на автомобиле марки'
# # Создайте целочисленную переменную cars_count = 0
# # Напишите в цикле из шага номер 2 увеличение переменной на 10
# # в каждом шаге цикла (cars_count += 10)
# car_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
# cars_count = 0
#
# while cars_count < 20:
#     for i in car_list:
#         print(f'My car is "{i}"')
#         cars_count += 2
#         print(f'My car is "{i}"' * cars_count)
#
#
#
#
# # пока не будет 50 яблок, добавлять по два)
# apple = 0
#
# while apple < 50:
#     apple += 2
#     print(apple)
#
#
#
# # Проверить входит ли введенное число в диапазон, если нет просим ввести число снова
#
# user_range = range(0, 10)
#
# while True:
#     user_input = int(input('Input digit: '))
#     if 0 <= user_input <= 10:
#         print('Digit in range!')
#         break
#
#
# # сравнить переменную со списком, если переменной в списке нет, искать дальше,
# # если переменная найдена в списке то закончить программу, используя цикл while
# cars_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
# user_car = input('Your cars?: ')
# found_car = False
#
# while not found_car:
#     for i in cars_list:
#         if i == user_car:
#             found_car = True
#             print(f'Car "{user_car}" found')
#             break
#     else:
#         user_car = input("Try again: ")
#
# print('car in list!')
#
# # Вводим число, если находится в списке, заканчиваем поиск, если нет - вводим снова
# my_list = [2, 4, 6, 8, 10]
# user_value = int(input('Input value:'))
# target_value = False
#
# while not target_value:
#     for i in my_list:
#         if i == int(user_value):
#             target_value = True
#             print(f'User value "{user_value}" is in list!')
#             break
#     else:
#         user_value = int(input('Try again!'))
# print('The end!')
#

# # Проверить входит ли введенное число в заданный диапазон, если нет просим ввести число снова

# # строку распечатать посимвольно
#
# str_1 = 'Hello World'
#
# for i in str_1:
#     print(i*5)
#

# # список распечать по строчно
#
# fruits = ['apple', 'banana', 'lemon']
# for fruit in fruits:
#     print(fruit)

# поиск по списку

year_times = ['January', 'February', 'March', 'April']
find_times = False
times_input = input('Enter a year time:')

while not find_times:
    if year_times.count(times_input):
        find_times = True
        print(f'The year time is {times_input} is in {year_times}')
        break
    else:
        times_input = input('Try again! Enter a year time:')


