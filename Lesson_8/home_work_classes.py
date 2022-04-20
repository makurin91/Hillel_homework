'''
Реализовать класс который бы производил разные операции над 2мя переданными числами.

Пример Использования:

proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add()).  выведет 30
print(proccess_input.subtract()).  выведет 10
print(proccess_input.multiple()).  выведет 200
print(proccess_input.divide()).  выведет 2
'''


class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_func(self):
        return self.a + self.b

    def subtract_func(self):
        return self.a - self.b

    def multiple_func(self):
        return self.a * self.b

    def divide_func(self):
        return self.a // self.b


class Test:
    cl = Calculate(4, 1)
    print(cl.add_func())
    print(cl.subtract_func())
    print(cl.multiple_func())
    print(cl.divide_func())
