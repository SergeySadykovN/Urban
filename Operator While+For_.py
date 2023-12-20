## Тренирую While For

# # Цикл по числам Фибоначи fib = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...

f1 = 1
f2 = 1
print(f1)
while f2 < 100:
    print(f2)
    next_f2 = f1 + f2
    next_f1 = f2
    f1 = next_f1
    f2 = next_f2

#Создайте список из 5 машин
# Создайте цикл for и в цикле распечатайте
# каждый из автомобилей в строке 'Я езжу на автомобиле марки'
# Создайте целочисленную переменную cars_count = 0
# Напишите в цикле из шага номер 2 увеличение переменной на 10
# в каждом шаге цикла (cars_count += 10)
car_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0

while cars_count < 20:
    for i in car_list:
        print(f'My car is "{i}"')
        cars_count += 2
        print(f'My car is "{i}"' * cars_count)




# пока не будет 50 яблок, добавлять по два)
apple = 0

while apple < 50:
    apple += 2
    print(apple)



# Проверить входит ли введенное число в диапазон, если нет просим ввести число снова

user_range = range(0, 10)

while True:
    user_input = int(input('Input digit: '))
    if 0 <= user_input <= 10:
        print('Digit in range!')
        break


# сравнить переменную со списком, если переменной в списке нет, искать дальше,
# если переменная найдена в списке то закончить программу, используя цикл while
cars_list = ["BMW", "MB", "LADA", "KIA", "HONDA"]
user_car = input('Your cars?: ')
found_car = False

while not found_car:
    for i in cars_list:
        if i == user_car:
            found_car = True
            print(f'Car "{user_car}" found')
            break
    else:
        user_car = input("Try again: ")

print('car in list!')

# Вводим число, если находится в списке, заканчиваем поиск, если нет - вводим снова
my_list = [2, 4, 6, 8, 10]
user_value = int(input('Input value:'))
target_value = False

while not target_value:
    for i in my_list:
        if i == int(user_value):
            target_value = True
            print(f'User value "{user_value}" is in list!')
            break
    else:
        user_value = int(input('Try again!'))
print('The end!')



fruit_list = ["apple", "banana", "juice"]
user_input = input('Enter your favorite fruit: ')
fruit_found  =  False

while not fruit_found:
    for fruit in fruit_list:
        if user_input == fruit:
            fruit_found = True
            print(f'The {fruit} is in list!')
            break
    else: user_input = input('Enter another fruit: ')
print('Search completed!')


# поиск числа в заданном диапазоне, пока не найдем повтрять


range_value = range(1, 20)
user_input = int(input("Enter a number: "))
target_value = False

while user_input != target_value:
    if user_input in range_value:
        target_value = True
        print(f'target_value is "{user_input}" is in range')
        break

    else:
        user_input = int(input(f'{user_input} is not in range,\nTry again!: '))
