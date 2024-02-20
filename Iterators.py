"""Напишите класс-итератор EvenNumbers для перебора чётных чисел
в определённом числовом диапазоне. При создании и инициализации объекта этого класса
создаются атрибуты:
start – начальное значение (если значение не передано, то 0)
end – конечное значение (если значение не передано, то 1)"""


class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.start <= self.end:
            if self.start % 2 == 0:
                numbers = self.start
            else:
                numbers = self.start + 1
            self.start += 2
            return numbers

        else:
            raise StopIteration


for i in EvenNumbers(1, 5):
    print(i)
for i in EvenNumbers(1, 3):
    print(i)

# value_iter = EvenNumbers(1,9)
# print(next(value_iter))
# print(next(value_iter))
