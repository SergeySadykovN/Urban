# '''Создайте новую функцию def test... с произвольным числом параметров
# разного типа, функция должна распечатывать эти параметры внутри своего тела'''
#
#
# def arbitrary_param(*args, **kwargs):
#     print(f'List of value: {args}')
#     # здесь по аргументам. принимаем список значений как кортеж, создаем и выводим список значений
#     for i, arg in enumerate(args):
#         print(f'Value {i}: {arg}')
#     # здесь  по ключам. принимаем именованные значения, создаем словарь с парой ключ:значение
#     print(f'Dict of value: {kwargs}')
#     for key, value in kwargs.items():
#         print(f'_________________________\nKey: {key:7}  Value: {value} ')
#
#
# # noname param
# print('\nResult by noname param: ')
# arbitrary_param(3, 'hello', 44.5)
# # named param
# print('\nResult by named param: ')
# arbitrary_param(number=3, name='Sanny', phone=9317777777, adress='Hello World')
# # mixed param
# print('\nResult by Mixed Param: ')
# arbitrary_param(1, 'Hello World', phone=931777777)
# # unpack
# print('\nResult by Unpacking: ')
# my_bio = {'name:': 'Sergey', 'age:': 20, 'height:': 178}
# arbitrary_param(**my_bio)
#
# '''Создайте рекурсивную функцию, которая будет считать факториал от числа n,
# n - передается в параметре'''
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     factorial_n_minus_1 = factorial(n=n - 1)
#     return n * factorial_n_minus_1
#
#
# find_factorial = 9
# print(f'_________________________\nFactorial: !{find_factorial} == {factorial(find_factorial)}')
#
# ''' Считаем сумму чисел от 1 до n, с помощью рекурсивной функции '''
#
#
# def summa(n):
#     if n == 1:
#         return 1
#     return n + summa(n - 1)
#
#
# n_value = 5
# print(f'_________________________\nsum of numbers from 1 to n({n_value}) = {summa(n_value)}')


# # проверка переменной . палиндром или нет, true or false
# # с помощью рекурсии
# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1: -1])


# print(palindrom('21'))
#
# # с помощью спец синтаксиса
# def palindrom_simple (s):
#     return s == s[::-1]
#     return s == s[len(s)-1::-1]
#
# print(palindrom_simple('srs'))

# # лист палиндром ?
#
# def is_palindrome(list):
#     return list == list[::-1]
#
#
# print(is_palindrome([1, 2, 3, 4, 5, 4, 3, 2, 1, ]))

# # c помощью рекурсии принять строку (asdfghjkl)  отдать a(s(d(f(g)h)j)k)l)
# def rec_f(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] + '(' + rec_f(s[1:-1]) + ')' + s[-1]
#
#
# print(rec_f('asdfgaskjdfgajsgdfjags'))

#
# def palindrome(string):
#     if len(string) <= 1:
#         return True
#     if string[0] != string[-1]:
#         return False
#     return palindrome(string[1:-1])
#
# print(palindrome('dffd'))

# palindrom int

# def is_palindrome(x):
#     str_x = str(x)
#     reversed_str_x = str_x[::-1]
#     return x == int(reversed_str_x)
#
# x = int(input())
#
# if is_palindrome(x):
#     print("true")
# else:
#     print("false")