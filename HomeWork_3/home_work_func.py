import random

"""
1) Заменить в произвольной строке согласные буквы на гласные.
"""


def change_func(some_str):
    vowels = 'aeiou'
    r = ''.join(letter if letter in vowels or not letter.isalpha() else random.choice(vowels) for letter in some_str)
    return r


my_string = 'some text for checking this func'
print(change_func(my_string))

"""
2) Дан массив из словарей
"""

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

"""
2.1) отсортировать массив из словарей по значению ключа ‘age'
"""


def sorting_arr(arr):
    sorted_list = sorted(arr, key=lambda y: y['age'])
    return sorted_list


print(sorting_arr(data))

"""
2.2) сгруппировать данные по значению ключа 'city'
"""


def group_by_city(some_arr):
    city_template = {x['city']: [] for x in some_arr}
    for x in some_arr:
        city = x.pop('city')
        name_age_dict = {key: value for key, value in x.items()}
        city_template[city].append(name_age_dict)
    return city_template


print(group_by_city(data))

"""
3) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
"""

some_list = ('a', 'a', 'bi', 'bi', 'bi')


def most_frequent(list_var):
    result = ''
    for i in list_var:
        if list_var.count(i) > list_var.count(result):
            result = i
    return result


print(most_frequent(some_list))
