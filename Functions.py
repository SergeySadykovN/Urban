# # Функция, которая  в своем теле печатает
# # переданное значение из параметра  2  раза
# def print_params(count):
#     """ функция печатает два раза """
#     print(count)
#     print(count)
#
#
# help(print_params)
# print_params('print twice')
# print_params('print twice  again!')
#
#
# # Функция суммирует заданные значения
# def summa(a, b, c):
#     """функция суммирует заданные значения"""
#     result = a + b + c
#     print(f'Result: {a} + {b} + {c} = {result} ')
#
#
# help(summa)
# print(' Input three integers:')
# print(summa(int(input('First value ')), int(input('Second value ')), int(input('Third value  '))))
#
#
# # Фунцкия принимает ФИО  и выводит полное ФИО
# def full_name(first_name, last_name, middle_name):
#     '''Фунцкия принимает ФИО  и выводит полное ФИО'''
#     return f'First Name: {first_name}\nSecond Name: {last_name}\nMiddle Name: {middle_name}'
#
#
# help(full_name)
# print(full_name(
#     first_name=input(f'Input first name: '),
#     last_name=input('Input last name: '),
#     middle_name=input('Input middle_name: ')))
#
#
# # Функция ищет заданном в диапазоне цифру пока не найдет
# def find_value(first_range, second_range, target_value):
#     '''Функция ищет в заданном диапазоне цифру пока не найдет'''
#     my_range = range(int(first_range), int(second_range))
#     find_value = False
#     while target_value != find_value:
#         if target_value in my_range:
#             find_value = True
#             print(f'Target value is found')
#             return target_value
#         else:
#             print('Not found')
#             target_value = int(input("Enter target value one more time : "))
#
#
# help(find_value)
# find_value(1, 10, int(input('Input target value: ')))
#
#
# функция ищет в списке фамилию, если есть - останавливаем поиск,
# если нет - предлагаем добавить фамилию в список и продлжаем поиск
def name_data(name_value):
    name_list = ['<Elena>', '<Anton>', '<Igor>', 'Serg']
    name_found = False

    while name_value != name_found:

        if name_value in name_list:
            name_found = True
            # сделать строчными буквы чтоб искал независимо от ввода Прописных или строчных КАК??
            name_value = name_value.lower()
            print(f'The name is {name_value.lower()} is in the list!')
            break
        else:
            name_list.append(name_value)
            print(f'The name is {name_value} is not in list!\nBut i add it to the list!')
            # name_list = name_list.append(name_value)
            print(name_list)



# name_data(name_value=input('Input your name: '))
