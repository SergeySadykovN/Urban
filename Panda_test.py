import numpy
import pandas as pd
import statistics
"""Считать данные из файла с помощью библиотеки pandas, 
выполнить простой анализ данных и вывести результаты."""

file_name = 'TestForPandas.csv'

# Чтение данных из CSV файла
data = pd.read_csv(file_name)
print(data)

# Среднее значение
mean_value = statistics.mean(data['count'])
print(f'average data from count: {mean_value}')

# добавление строчки
new_row = ['', 'Average', mean_value]
data = data._append(new_row, ignore_index=True)

# сохранение файла
data.to_csv('output.csv', index=False)





