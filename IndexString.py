'''Создайте переменную с именем my_string и присвойте ей значение строки
(любой фразы или предложения).'''

my_string = 'Test_string'
print(f'String: {my_string}')
'''3. Используя индексацию строк, выполните следующие действия:'''

# Выведите первый символ строки my_string.
print(f'first char in the string: {my_string[0]}')
# Выведите последний символ строки my_string.
print(f'last char in the string: {my_string[-1]}')
# Выведите подстроку строки my_string с третьего по шестой символы.
print(f'string from the third to the fifth character: {my_string[2:5]}')
# Выведите длину строки my_string.'''
print(f'length of the string: "{my_string}" = {len(my_string)}')

'''4. Используя операции конкатенации строк, выполните следующие действия:
Создайте переменную с именем another_string и присвойте ей значение строки.'''

another_string = 'Combined'

# Соедините строки my_string и another_string и сохраните результат
# в новую переменную: new_string = my_string + another_string
# Выведите полученную строку на экран
new_string = another_string +' '+ my_string
print(f'Combined string: {new_string}')

