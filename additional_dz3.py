from functools import reduce
import re

"""
8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Например:
Дано число 123405. Результат будет: 1*2*3*4*5=120.
"""

some_numb = 123405


def multiply_digits(x_numb):
    iterable_list = list(str(x_numb))
    iterable_list.remove('0')
    return reduce(lambda x, y: int(x) * int(y), iterable_list)


print(multiply_digits(some_numb))

"""
9) Есть массив с положительными числами и число n (def some_function(array, n)).
Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
"""

data = [1, 2, 3, 4, 5, 6]


def some_function(array, n):
    if n in range(array[0], array[-1]):
        return array[n] ** n
    elif array[n - 1] is len(array):
        return array[n - 1] ** n
    return -1


print(some_function(data, 6))

"""
10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
"""

some_string = 'hello 1 one two three 15 world'


def check_matches(text):
    match = re.search(r'\s+'.join([r'[^\d\s]+'] * 3), text)
    return 'True' if bool(match) is True else 'False'


print(check_matches(some_string))
