import warnings


def division_function(dividend, divisor):
    if divisor <= 0.01:
        warnings.warn('Warning: Division by nearly zero.')
    return dividend / divisor


warnings.filterwarnings('always') #выбрасывает варнинг всегда
# warnings.filterwarnings('ignore') #игнорирует варнинг

print(division_function(10, 0.01))

#
# warnings.filterwarnings(action='error')
# try:
#     print(division_function(3, 0))
# except ValueError as e:
#     # При возникновении ошибки вместо предупреждения
#     # будет выброшено исключение
#     print('Error message: { }')
