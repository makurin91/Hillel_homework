import functools

'''
Реализовать класс который бы производил разные операции над 2мя переданными числами.

Пример Использования:

proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add()).  выведет 30
print(proccess_input.subtract()).  выведет 10
print(proccess_input.multiple()).  выведет 200
print(proccess_input.divide()).  выведет 2
'''


def checking_division(func):
    @functools.wraps(func)
    def wrap(*args):
        try:
            print(int(func(*args)))
        except TypeError:
            return 'You need to enter only digits'
    return wrap


class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @checking_division
    def add_func(self):
        return self.a + self.b

    @checking_division
    def subtract_func(self):
        return self.a - self.b

    def multiple_func(self):
        if self.a and self.b is int:
            return self.a * self.b
        else:
            return 'You need to enter only digits'

    @checking_division
    def divide_func(self):
        return self.a // self.b


class Test:
    cl = Calculate(10, 's')
    print(cl.add_func())
    print(cl.subtract_func())
    print(cl.multiple_func())
    print(cl.divide_func())
