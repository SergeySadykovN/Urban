import inspect
from pprint import pprint
import faker


class Man_can:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_param(self):
        print(f'{self.name} age: {self.age}')

    def mean(self, age_list):
        print(sum(age_list)/len(age_list))




def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['module'] = obj.__module__
    info['attributes'] = [attr_name for attr_name, attr_value in vars(obj).items() if not callable(attr_value)]
    info['methods'] = [meth_name for meth_name in dir(obj) if not meth_name.startswith('__')]
    if inspect.isclass(obj): # Проверяем, является ли объект классом
        info['class_attrs'] = ['__module__', '__name__', 'mro']
    elif inspect.ismethod(obj): # Проверяем, является ли объект методом
        info['method_args'] = inspect.getfullargspec(obj)[0]
    return info







obj = introspection_info(Man_can)
pprint(obj)


