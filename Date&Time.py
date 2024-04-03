import time
from datetime import datetime

"""Создайте класс SuperDate, наследованный от класса datetime модуля datetime, 
объекты которого будут дополнительно обладать следующими методами:

1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток
(Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)


Пример работы класса:

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())"""


class SuperDate(datetime):

    def get_season(self):
        """должен возвращать сезон года
        (Summer, Autumn, Winter, Spring)"""
        seasons = {
            'Winter': (11, 0, 1),
            'Spring': (2, 3, 4),
            'Summer': (5, 6, 7),
            'Autumn': (8, 9, 10)
        }
        for season, period in seasons.items():
            if period.count(self.month):
                return season
            else:
                raise ValueError('Invalid date')

    def get_time_of_day(self):
        """должен возвращать  время суток
        (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6)"""
        day_time = {
            'Morning': range(6, 12),
            'Day': range(12, 18),
            'Evening': range(18, 24),
            'Night': range(0, 6)
        }
        for times, period in day_time.items():
            if period.count(self.hour):
                return times


my_date = SuperDate(2024, 11, 22, 22)
print(f'Desired date: {my_date.get_season()}, {my_date.get_time_of_day()}')

