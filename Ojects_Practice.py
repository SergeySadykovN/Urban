class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 100
        self.money = 0

    def __str__(self):
        return ('я - {}, сытось {}, осталось еды {}, денег осталось {} '
                .format(self.name, self.fullness, self.food, self.money))

    def eat(self):
        if self.food > 10:
            print('поел '.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('еды нет'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50


Sergey = Man(name='Sergey')
Andrew = Man(name='Andrew')
print(Sergey)
Sergey.eat()
print(Sergey)
Sergey.work()
print(Sergey)
Andrew.work()
print(Andrew)

