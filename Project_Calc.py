class Calculator:
    first_value = int(input("Enter first number: "))
    sign = str(input("Enter the sigh: "))
    second_value = int(input("Enter second: "))
    result = None

    def __init__(self, first_value, sign, second_value):
        self.first_value = first_value
        self.sign = sign
        self.second_value = second_value
        self.result = 0

    def checker(self):
        """проверить символы на валидность"""
        first_value = self.first_value
        sign = self.sign
        second_value = self.second_value
        pass

    def calculate(self):
        """калькулятор"""
        # if self.first_value.isnumeric():
        pass


test = Calculator(1, 1, 1)
