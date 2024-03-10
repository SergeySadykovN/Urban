import numpy
import matplotlib.pyplot as plt


'''Создать массив чисел с помощью библиотеки numpy, 
выполнить математические операции с массивом и вывести результаты.'''


# создадим массив размером 10x2, заполненный значениями от 0 до 9:
list_numphy = numpy.array([[i for i in range(10) for j in range(2)]])
for row in list_numphy:
    print(f'Create row: {row}')

# среднее значение каждого элемента массива
list_numphy_average = numpy.mean(list_numphy, axis=1)
print(f'Mean value of each elements in: {list_numphy} = {list_numphy_average} ')

# мин и макс  значений массива
max_of_list = numpy.max(list_numphy)
min_of_list = numpy.min(list_numphy)
print(f'Min value: {min_of_list}\nMax value: {max_of_list}')

# сумма всех значений в массиве
sum_of_list = numpy.sum(list_numphy)
print(f'Sum of list: {sum_of_list}')


'''Визуализировать данные с помощью библиотеки matplotlib.'''

min_value, max_value = min(row), max(row)
plt.plot(row)
plt.xlabel('‘Значения’')
plt.ylabel("‘График’")
plt.title("‘График с минимальным и максимальным значениями’")
plt.grid(linestyle='-', linewidth=0.5)
plt.axhline(y=min_value, color='r', linestyle='-', linewidth=1)
plt.axvline(x=min_value, color='g', linestyle=':', linewidth=1)
plt.savefig('graph.png')
plt.show()


