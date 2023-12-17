''' Функции с параметрами по умолчанию '''

'''Simple'''


def update_features(soft=None, hard='update yet', skills='update yet'):
    print(f'soft : {soft}')
    print(f'hard : {hard}')
    print(f'skills : {skills}\n')


# no args
print('no args: \n________________')
update_features()
# 1 unnamed args
print(f'1 unnamed args: \n________________')
update_features('Is update!')
# 3 named args
print('3 named args:  \n________________')
update_features('Is update!', hard='Is update!', skills='Updated!!')
# 2 named args
print('2 named args:  \n________________')
update_features('Is update!', skills='Updated!!')

'''Функция с параметрами по умолчанию:
Создайте функцию print_params(a, b, c), которая принимает три параметра со значениями 
по умолчанию (например: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])'''


def print_params(a=777, b='Strong', c=True):
    print(f'a: {a}, b: {b}, c: {c} ')


# none args
print_params()
# 1 named args
print_params(b='Strongest!')
# 2 unnamed args
print_params(666, 'Fool')
# 3 named args
print_params(888, b='Strongest!', c=False)
# check print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)  # valid
print_params(c=[1, 2, 3])  # valid

'''Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции 
print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя 
распаковку параметров (* для списка и ** для словаря).'''

values_list = [1000, 'Best!', True]
values_dict = {'a': 555, 'b': 'NoBad!', 'c': False}

# unpack value_list
print(f'_____________________\nUnpacked values_list:')
result = print_params(*values_list)
# unpack value_dict
print(f'_____________________\nUnpacked values_dict:')
result = print_params(**values_dict)

'''Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)'''

values_list_2 = ['String', 333]
print(f'__________________________________\nUnpack with 2nd list: ', values_list_2)
print_params(*values_list_2)
# check for print_params(*values_list_2, 42)
print(f'__________________________________\nCheck "print_params(*values_list_2, 42)":')
print_params(*values_list_2, 42)
