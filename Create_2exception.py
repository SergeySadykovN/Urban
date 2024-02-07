"""Создайте новый проект или продолжите работу в текущем проекте.
Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
Например, InvalidDataException и ProcessingException.
Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
В основной части программы вызовите эти функции и корректно обработайте"""


class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = "Ошибка данных: "
        print(self.message)


class ProcessingException(Exception):
    def __init__(self, message):
        self.message = "Ошибка процесса: "
        print(self.message)


def generator_exceptions(message):
    """Генерируем исключения"""
    if message == 'InvalidDataException':
        raise InvalidDataException('Invalid Data')
    elif message == 'ProcessingException':
        raise ProcessingException('Processing error')


def call_generator_example():
    """Обработка исключений"""
    try:
        generator_exceptions('InvalidDataException')
    except InvalidDataException as e:
        print(f'Data error: {e}')

    try:
        generator_exceptions('ProcessingException')
    except ProcessingException as e:
        print(f'Processing error: {e}')


call_generator_example()
