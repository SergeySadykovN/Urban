def string_to_int(string):
    """add exception ValueError"""
    try:
        return int(string)
    except ValueError:
        return 'Invalid input'


print(string_to_int('s'))  # Invalid input
print(string_to_int('4'))  # 4 (int)


def read_file(file_name):
    '''add exception FileNotFoundError, IOError'''
    try:
        with open(file_name, 'r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        return 'FileNotFoundError: File not found'
    except IOError:
        return 'IOError: input-output error'
    except UnicodeError:
        return 'UnicodeError:'


print(read_file('poem about winter.txt'))  # printed content
print(read_file('test.txt'))  # File not found


def divide_numbers(a, b):
    """add exception ZeroDivisionError, TypeError"""
    try:
        return a / b
    except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"
    except TypeError:
        return 'TypeError: every element must be a number'


print(divide_numbers(6, 's'))  # TypeError: every element must be a number
print(divide_numbers(5, 0))  # ZeroDivisionError: division by zero
print(divide_numbers(6, 3))  # 2.0


def access_list_element(lst, index):
    """ add exception IndexError, TypeError"""
    try:
        return lst[index]
    except IndexError:
        return "IndexError:"
    except TypeError:
        return 'TypeError:'


print(access_list_element([1, 2, 3], 0))  # printed 1 (first element in list, for index 1 )
print(access_list_element([1, 2, 3], 4))  # IndexError (index 4 is not exist)
print(access_list_element(3, 3))  # TypeError (must be list and index)
