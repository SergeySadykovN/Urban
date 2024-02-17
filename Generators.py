def all_subsequence(string):
    '''Напишите функцию-генератор all_variants,
    которая будет возвращать все подпоследовательности переданной строки.
    В функцию передаётся только сама строка'''
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            yield string[i:j]


for substr in all_subsequence('abcd'):
    print(substr)
# a
# ab
# abc
# abcd
# b
# bc
# bcd
# c
# cd
# d


def generator_fibonacci():
    '''генератор чисел фибоначи'''
    a, b = 0, 1
    while a < 50:
        yield a
        a, b = b, a + b


for fib_num in generator_fibonacci():
    print(fib_num)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


def generator_name(name_list):
    '''генератор вывода  зачений списка по очереди'''
    for name in name_list:
        yield name


name_next = generator_name(['Serg', 'Anna', 'Anton'])
# print(next(name_next))#Serg
# print(next(name_next))#Anna
# print(next(name_next))#Anton

for name in name_next:
    print(name)
# Serg
# Anna
# Anton
