'''Работа со списками:'''
# - Создайте переменную my_list и присвойте ей список из нескольких элементов,
my_list = ['Apple', 'Banana', 'Cherry', 'Lemon', 'Orange', 'Pear']
# - Выведите на экран список my_list.
print(f'List of the fruits: {my_list}')
# - Выведите на экран первый и последний элементы списка my_list.
print(f'First fruit: {my_list[0]}, last fruit: {my_list[-1]}')
# - Выведите на экран подсписок my_list с третьего до пятого элементов.
print(f'from third to fifth fruit: {my_list[2:5]}')
# - Измените значение третьего элемента списка my_list.
my_list[2] = 'SuperCherry'
# - Выведите на экран измененный список my_list.
print(f'Change the value of the third element of the list {my_list}')

'''Работа со словарями:'''
# - Создайте переменную my_dict и присвойте ей словарь с парами ключ-значение,
# например, переводами некоторых слов.
my_dict = {'Apple': 'Яблоко', 'Banana': 'Банан', 'Cherry': 'Вишня', 'Lemon': 'Лемон'}
# - Выведите на экран словарь my_dict.
print(f'\nDict word translation: {my_dict}')
# - Выведите на экран значение для заданного ключа в my_dict.
print(f'value of dict by key: "Lemon" = {my_dict.get("Lemon")}')
# - Измените значение для заданного ключа в my_dict.
my_dict['Lemon'] = 'Супер Лемон!'
# - Выведите на экран измененный словарь my_dict.
print(f'Changed dict: {my_dict}')
