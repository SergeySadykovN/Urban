'''Организуйте программу:
Создайте переменную my_string и присвойте ей значение строки с произвольным текстом.
Выведите на экран длину строки.'''

my_string = "String methods for practicing"
print(f'Length of the String : "{my_string}" = {len(my_string)}')

'''Работа с методами строк:
Используя методы строк, выполните следующие действия:'''

#Выведите строку my_string в верхнем регистре.
print(f'String UPPER: {my_string.upper()}')
#Выведите строку my_string в нижнем регистре.
print(f'String LOWER: {my_string.lower()}')
#Измените строку my_string, удалив все пробелы.
print(f'String without spaces: {my_string.replace(' ','')}')
#Выведите первый символ строки my_string.
print(f'First char of the strinh: {my_string[0]}')
#Выведите последний символ строки my_string.
print(f'Last char of the strinh: {my_string[-1]}')
