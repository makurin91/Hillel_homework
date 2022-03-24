""""
1) Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
"""
numbers = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(numbers)

"""
1.1) убрать из него повторяющиеся элементы
"""
uniq_numb = list(set(numbers))
print(uniq_numb)
"""
1.2) вывести 3 наибольших числа из исходного массива 
"""
max_one = max(numbers)
max_two = max(x for x in numbers if x != max_one)
max_tree = max(y for y in numbers if y != max_one if y != max_two)
print(max_one, max_two, max_tree)
"""
1.3) вывести индекс минимального элемента массива
"""
min_digit = min(uniq_numb)
index_min_digit = uniq_numb.index(min_digit)
print(index_min_digit)
"""
1.4) вывести исходный массив в обратном порядке
"""
print(sorted(numbers, reverse=True))

"""
2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
"""
generated_digits = list(range(0, 101))
even_digit = [i for i in generated_digits if i % 2 == 0]
print(even_digit)

"""
3) Найти общие ключи в двух словарях:
"""
dict_one = {'a': 1, 'b': 2, 'c': 3,  'd': 4}
dict_two = {'a': 6,  'b': 7, 'z': 20, 'x': 40}
for k in dict_one:
    for j in dict_two:
        if k == j:
            print(k.split(), end='')

"""
4) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key)
"""
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generated_dict = {}
for i in keys:
    generated_dict[i] = i * i
print(end='\n')
print(generated_dict)