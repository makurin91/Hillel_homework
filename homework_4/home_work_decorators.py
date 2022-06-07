import functools

"""
ЗАДАЧА-1
Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции.
Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
"""


def checking_remainder_of_the_division(func):
    def wrapper(*args):
        result = 100 % func(*args)
        if result == 0:
            print('We are OK!')
        else:
            print(f'Bad news guys, we got {result}')

    return wrapper


@checking_remainder_of_the_division
def func_for_rev_division(some_numb):
    return some_numb


func_for_rev_division(9)

"""
ЗАДАЧА-2
Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
Если это int, тогда выполнить функцию и вывести результат, если это str(),
тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))
"""


def decorator_for_checking_type_of_the_value(func):
    def wrapper_around_the_func(*args):
        try:
            print(int(func(*args)))
        except ValueError:
            raise ValueError('String type is not supported')

    return wrapper_around_the_func


@decorator_for_checking_type_of_the_value
def pr_some_value(b):
    return b


pr_some_value('This if string')

"""
*ЗАДАЧА-3
Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
«Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
количество раз обращений в cache.
"""


def decorator_count(func):
    cache = {}

    @functools.wraps(func)
    def wrap(*args):
        if args in cache:
            wrap.call += 1
            print(f'Used cache with counter = {wrap.call}')
            return cache[args]
        else:
            wrap.ncall += 1
            cache[args] = func(*args)
            print(f'Function executed with counter = {wrap.ncall}, function result = {cache[args]}')
            return cache[args]

    wrap.call = 0
    wrap.ncall = 0
    return wrap


@decorator_count
def sum_numb(n):
    return n + n


sum_numb(2)
sum_numb(1)
sum_numb(1)
sum_numb(10)
sum_numb(10)
sum_numb(10)
sum_numb(2)
