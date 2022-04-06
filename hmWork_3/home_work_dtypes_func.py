from collections import defaultdict

'''
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

1.1) Выведите элемент коллекции с индексом 4
1.2) Добавить число 10 в конец списка
1.3) Удалить элемент из списка под индексом 10
1.4) Выведите все элементы, которые меньше 5.
1.5) Выведите первый и последний элемент списка.
1.6) Выведите чётные числа из заданного списка
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''1.1'''
print(a[4])
'''1.2'''
a.append(10)
print(a)
'''1.3'''
del a[10]
print(a)
'''1.4'''
print(list(x for x in a if x < 5))
'''1.5'''
print(a[0], a[-1])
'''1.6'''
print(list(y for y in a if y % 2 == 0))


'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].

1.7) Объеденить 2 списка в один список
1.8) Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
''''1.7'''
print(a+b)
''''1.8'''
print(list(x for x in a for y in b if x == y))

'''
dict

Создать словарь который содержит имена и возраст пользователей. (напр. {'name': 'Vasia', 'age': 30})
2.1) Добавить к существующему словрю еще одно имя.
2.2) Удалить пользователя из словаря с конкретным именем(напр. "Vasia")
2.3) Отсортировать словарь по значению age
'''

'''2.0'''
dict_example = {'name': 'Vasya', 'age': 30}

'''2.1'''

dict_example['name'] = {'Vasya', 'Alex'}
print(dict_example)


'''2.2'''
dict_example['name'].remove('Vasya')
print(dict_example)

'''2.3'''

'''
set

Создать 2 сета
3.1) найти общие елементы у двух сетов
3.2) найти разницу между двумя сетами
3.3) добавить значение в сет
3.4) удалить значение из сета
'''

'''3.0'''
a = {1, 2, 3, 4}
b = {0, 2, 4, 7}
'''3.1'''
print(a.intersection(b))
'''3.2'''
print(a.symmetric_difference(b))
'''3.3'''
a.add(5)
print(a)
'''3.4'''
a.discard(1)
print(a)


'''
srt
создать строку
4.1) получить первый элемент строки
4.2) получить последний элемент строки
4.3) получить 5-й элемент строки
4.4) добавить символ к строке
4.5) заменить все пробелы в строке на '_'
4.6) есть лист ['h', 'e', 'l', 'l', 'o']. Преобразовать его в строку 'hello'
4.7) поработать с форматом строки. Например:
name = 'Vasia'
"Hello {} world".format(name) или тоже самое но более нового вида формат
f"Hello {name} world"
'''

'''4.0'''
new_str = 'Some String'
'''4.1'''
print(new_str[0])
'''4.2'''
print(new_str[-1])
'''4.3'''
print(new_str[5])
'''4.4'''
print(new_str + ' Added')
'''4.5'''
print(new_str.replace(' ', '-'))
'''4.6'''
test = ['h', 'e', 'l', 'l', 'o']
print(''.join(test))
'''4.7'''
name = 'Ivan'
print('Hello {}'.format(name))
print(f'Hello {name}')
