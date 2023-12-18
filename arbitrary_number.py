'''Создайте новую функцию def test... с произвольным числом параметров
разного типа, функция должна распечатывать эти параметры внутри своего тела'''


def arbitrary_param(*args, **kwargs):
    print(f'List of value: {args}')
    # здесь по аргументам. принимаем список значений как кортеж, создаем и выводим список значений
    for i, arg in enumerate(args):
        print(f'Value {i}: {arg}')
    # здесь  по ключам. принимаем именованные значения, создаем словарь с парой ключ:значение
    print(f'Dict of value: {kwargs}')
    for key, value in kwargs.items():
        print(f'_________________________\nKey: {key:7}  Value: {value} ')


# noname param
print('\nResult by noname param: ')
arbitrary_param(3, 'hello', 44.5)
# named param
print('\nResult by named param: ')
arbitrary_param(number=3, name='Sanny', phone=9317777777, adress='Hello World')
# mixed param
print('\nResult by Mixed Param: ')
arbitrary_param(1, 'Hello World', phone=931777777)
# unpack
print('\nResult by Unpacking: ')
my_bio = {'name:': 'Sergey', 'age:': 20, 'height:': 178}
arbitrary_param(**my_bio)

'''Создайте рекурсивную функцию, которая будет считать факториал от числа n,
n - передается в параметре'''


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1


find_factorial = 9
print(f'_________________________\nFactorial: !{find_factorial} == {factorial(find_factorial)}')

''' Считаем сумму чисел от 1 до n, с помощью рекурсивной функции '''


def summa(n):
    if n == 1:
        return 1
    return n + summa(n - 1)


n_value = 5
print(f'_________________________\nsum of numbers from 1 to n({n_value}) = {summa(n_value)}')
