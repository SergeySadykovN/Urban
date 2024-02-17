"""Напишите класс-итератор EvenNumbers для перебора чётных чисел
в определённом числовом диапазоне. При создании и инициализации объекта этого класса
создаются атрибуты:
start – начальное значение (если значение не передано, то 0)
end – конечное значение (если значение не передано, то 1)"""


class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            numbers = self.start if self.start % 2 == 0 else self.start + 1
            self.start += 2
            return numbers

        else:
            raise StopIteration


# чтобы четные значения вывести списком
even_list = []
for i in EvenNumbers(1, 10):
    even_list.append(i)
print(even_list)
# [2, 4, 6, 8, 10]


# просто вывести построчно
for i in EvenNumbers(1, 6):
    print(i)
# 2
# 4
# 6
