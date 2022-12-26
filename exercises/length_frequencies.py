
data = ("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
    minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.""".split())

print(data)

def length_frequencies(data):
    dict_count = {}
    for i in data:
        if len(i) in dict_count:
            dict_count.update({len(i): dict_count.get(len(i)) + 1})
        else: 
            dict_count.update({len(i): 1})
    return dict_count

print(length_frequencies(data))

'''
Вам необходимо реализовать функцию length_frequencies(), 
которая принимает последовательность (iterable) слов (строк) в качестве единственного аргумента 
и возвращает словарь, ключами которого выступают длины слов, а значениями — количество слов соответствующей длины.

from solution import length_frequencies
length_frequencies([])  # {}
length_frequencies(['abcde'])  # {5: 1}
length_frequencies(['a', 'b', 'c'])  # {1: 3}
length_frequencies('Use the Force, Luke!'.split())  # {3: 2, 5: 1, 6: 1}

Это задание можно выполнить в процедурном стиле с помощью defaultdict или dict.setdefault, 
однако попробуйте описать декларативное решение с использованием comprehensions. Возможно, 
вам пригодится функция itertools.groupby().
'''