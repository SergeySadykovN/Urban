import queue
from threading import Thread
from time import sleep
import time


class Table:
    '''класс для столов, который будет содержать следующие атрибуты:
        number(int) - номер стола, is_busy(bool) - занят стол или нет'''
    def __init__(self, id):
        self.id = id
        self.is_busy = False


class Cafe:
    '''класс для симуляции процессов в кафе.'''
    def __init__(self, queue, tables):
        self.queue = queue
        self.tables = tables

    def customer_arrival(self):
        '''моделирует приход посетителя(каждую секунду)'''
        for customer_num in range(20):
            print(f'Посетитель номер {customer_num} прибыл')
            self.serve_customer(customer_num)
            sleep(1)

    def serve_customer(self, customer_num):
        '''моделирует обслуживание посетителя
                Проверяет наличие свободных столов, в случае наличия стола -
               начинает обслуживание посетителя (запуск потока),
               в противном случае - посетитель поступает в очередь.
               Время обслуживания 5 секунд.'''
        flag = False
        for table in self.tables:
            if table.is_busy == False:
                some_customer = Customer(customer_num, self, table)
                some_customer.start()
                flag = True
                break
            flag == False
            self.queue.put(customer_num)



class Customer(Thread):
    '''класс (поток) посетителя. Запускается, если есть свободные столы'''
    def __init__(self, id, cafe, table, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.cafe = cafe
        self.table = table

    def run(self):
        self.table.is_busy = True
        print(f'посетитель {self.id} сел за стол {self.table.id}. Начало обслуживания')
        sleep(5)
        print(f'посетитель {self.id} покушал и ушел. Конец обслуживания')
        self.table.is_busy = False
        if self.cafe.queue.qsize() > 0:
            self.cafe.serve_customer(self.cafe.queue.get())


tables = [Table(i) for i in range(1,4)]
queue = queue.Queue()
cafe = Cafe(queue, tables)


customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
