# Задачи для тренировки понимания оператора if


# 1.Программа для проверки, находится ли число в пределах от 0 до 100 .

'''Функция приводит  введенный символ числа к int
чтобы потом сравнить с указанным диапазоном '''


def in_range(n):
    if int(n) in range(0, 100):
        print('Value in the range')
    else:
        print('Value is not in the range')


print(in_range(input('Input value to found it in the range ')))

# 2. Программа , чтобы получить разницу между заданным числом и 17,
# если число больше 17, верну двойную  разницу.

input_value = input('input value to be compared: ')
target_value = 17

# сравниваю введенное число с 17, если число больше 17 вычисляю и возвращаю разницу и умножаю на 3
if (int(input_value) > int(target_value)):
    print('Target input > target_value with DOUBLE difference in values: ')
    print(((int(input_value) - int(target_value))) * 2)
else:
    # если число меньше 17, просто вычисляю и возвращаю разницу
    print('Target input < target_value DOUBLE difference in values: ')
    print(int(target_value) - int(input_value))

# 3. Программа для расчета суммы трех заданных чисел,
#  если значения равны, тогда верну их тройную  сумму.

'''Функция сравнивает числа. Если числа равны, складывает их и умножает на 3, 
 если нет - просто суммирует их'''


def summ(a, b, c):
    if a == b == c:
        sum = ((a + b + c) * 3)
    else:
        sum = a + b + c
    return sum


# здесь вводим числа для проверки и сложения

print('If values are equals: ' + str(summ(2, 2, 2)))
print('If values are different: ' + str(summ(1, 2, 3)))

# 4. Программа для поиска Имени в списке. Если Имя есть, то просто возвращаем что имя в списке,
# Если нет - добавляем в список введенное имя


name_list = ['Serg', 'Anna', 'Igor']
user_input = input('Input name: ')

if name_list.count(user_input):
    print('Name in list yet!')
else:
    name_list.append(user_input)
    print('Name  is not in list, but i add it  to the list :' + str(name_list))
