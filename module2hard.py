import random

# Генерация случайного числа от 3 до 20
rand_num = random.randrange(3, 20)

# Создание списка чисел от 1 до rand_num включительно
range_rand_nums = list(range(1, rand_num + 1))

# Определение длины списка
length = len(range_rand_nums)

# Создание пустого списка для пар чисел
res_list = []

# Вложенные циклы для поиска пар чисел
for i in range(length):
    x = range_rand_nums[i]
    for j in range(i + 1, length):
        y = range_rand_nums[j]
        # Проверка условий: x и y разные, сумма делится на rand_num
        if (x != y) and rand_num % (x + y) == 0:
            res_list.append((x, y))

# Создание строки результата из пар чисел
result_str = ""
for r in res_list:
    result_str += "".join(map(str, r))

# Печать случайного числа и строки результата
print(rand_num)
print(result_str)
