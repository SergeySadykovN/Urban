""" Здесь создал Исключение для работы принтера"""


class ExceptionPrintData(Exception):
    """Класс исключений при отправке принтеру данных"""
    pass


class PrintData:
    def print_data(self, data):
        """ф-ция печати на принтере"""
        self.send_data(data)
        print(f'print: {str(data)}')

    def send_data(self, data):
        """ф-ция  проверки отправки данных на принтер"""
        if not self.send_to_print(data):
            raise ExceptionPrintData("принтер не найден")

    def send_to_print(self, data):
        """ф-ция имитирующая ошибку отправки данных на принтер.
        False = выбросит исключение,
        True = выполнится печать"""
        return False


file_to_print = PrintData()
# file_to_print.print_data('123') # выбросит ExceptionPrintData

# обработка исключений
try:
    file_to_print.print_data('123')
except ExceptionPrintData:
    print('принтер не отвечает')
