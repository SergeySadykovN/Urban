'''Задание:
Моделирование программы для управления данными о движении товаров на складе и
эффективной обработки запросов на обновление информации в многопользовательской среде.

Представим, что у вас есть система управления складом, где каждую минуту поступают запросы
на обновление информации о поступлении товаров и отгрузке товаров.
Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы
в многопользовательской среде, с использованием механизма мультипроцессорности
для обеспечения быстрой реакции на поступающие данные.'''

from multiprocessing import Process, Pipe


class WarehouseManager(Process):
    def __init__(self, request, connect, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.data = {}
        self.request = request
        self.connect = connect

    def process_request(self):
        '''реализует запрос (действие с товаром), принимая request - кортеж.'''
        req = self.request
        if req[1] == 'receipt':
            self.data[req[0]] = req[2]
        if req[1] == 'shipment':
            if self.data[req[0]] >= req[2]:
                self.data[req[0]] -= req[2]
            else:
                self.data[req[0]] = 0
        self.connect.send(self.data)
        self.connect.close()

    def run(self):
        '''принимает запросы и создаёт для каждого свой параллельный процесс,
        запускает его(start) и замораживает(join).'''
        for self.request in requests:
            pr = Process(target=self.process_request)
            pr.start()
            self.data = parent_connect.recv()
            pr.join()


if __name__ == '__main__':
    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    """два объекта-дескриптора (parent_connect и child_connect), 
    которые представляют собой соединение двух концов канала связи (pipe). 
    Канал позволяет организовать передачу данных между процессами, 
    один из которых (parent_connect) является родительским, а другой (child_connect) - дочерним. 
    Когда данные записываются в один конец канала, они автоматически читаются из другого конца, и наоборот."""
    parent_connect, child_connect = Pipe()

    # Создаем менеджера склада
    manager = WarehouseManager(requests, child_connect)

    # Запускаем обработку запросов
    manager.run()

    # Выводим обновленные данные о складских запасах
    print(manager.data)
