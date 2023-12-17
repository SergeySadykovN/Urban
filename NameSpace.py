'''Создайте новую функцию def test...
1. Создайте две переменные a и b внутри пространства имен функции test
2. Распечатайте a и b внутри функции test
3. Создайте функцию def test2 с тремя параметрами, функция должна распечатывать все три параметра внутри своего тела'''


# 1-2
def test(a, b):
    print(F'RESULT FROM FUNCTION: {a, b}')


test(5, 6)


# print(a, b ) здесь а и b не видны

# 3
def test2(x, y, *, z):
    print(f'result from second function: {x, y, z}')


test2(1, 2, z=3)

# 4 Инициируем две глобальные переменные , а внутри функции меняем их. Выводим  глобальный результат и из функции
# НО ТАК ЛУЧШЕ НЕ ИСПОЛЬЗОВАТЬ!

global_1 = 'Global'
global_2 = 365
print(f'global_1 is {global_1}, global_2 is {global_2}')


def local_name():
    # эти переменные работают только внутри функции
    global_1 = 'local_name'
    global_2 = 180
    print(f'local is {global_1}, local is {global_2}')


local_name()
print(f'global 1 is {global_1}, global 2 is {global_2}')


