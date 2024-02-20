class Evennumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        '''выисляем четные числа'''
        if self.start % 2 == 1:
            self.value = self.start - 1
        else:
            self.value = self.start
        return self

    def __next__(self):
        '''пошагово +=2 '''
        if self.value > self.end:
            raise StopIteration
        else:
            self.value += 2
            return self.value


evn = Evennumbers(1, 7)
for i in evn:
    print(i)
for i in evn:
    print(i)
