class Calculator:
    first_value = int
    sign = str
    second_value = int
    result = None
    print_ex = '{}  {}  {} = {}'.format(first_value, sign, second_value, result)

    def __init__(self, *args, **kwargs):
        self.first_value = input("Enter first number: ")
        self.sign = input("Enter the sigh: ")
        self.second_value = input("Enter second: ")
        self.result = 0


class Checker(Calculator):
    """проверить символы на валидность"""
    pass


class Calc(Calculator, Checker):
    """калькулятор"""
    result = int
    pass




test = Calculator()
print(Calculator.print_ex)
