def is_prime(func):
    '''Функция декоратор (is_prime), которая распечатывает "Простое",
    если результат 1ой функции будет простым числом и
    "Составное" в противном случае.'''

    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 0:
            raise Exception(f'{n} is negative numbers cannot be simple or composite')
        if n == 0:
            raise Exception('The number 0 is neither a prime nor a composite number')
        elif n == 1:
            return f'{n} is prime'
        elif n == 2:
            return f'{n} is composite'
        else:
            for i in range(2, n):
                if n % i == 0:
                    return f'{n} is composite'
                return f'{n} is prime'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# print(sum_three(0, 0, -1))# Exception: negative numbers cannot be simple or composite
# print(sum_three(0, 0, 0))# The number 0 is neither a prime nor a composite number
print(sum_three(1, 2, 3))  # 6 is composite
print(sum_three(0, 0, 1))  # 1 is prime
