
from collections import Counter

word = 'abba'
list_word = ['aabb', 'abcd', 'bbaa', 'dada']

def filter_anagrams(word, list_word):
    anagramms_list = []
    for i in list_word:
        if Counter(i) == Counter(word):
            anagramms_list.append(i)
    return anagramms_list

print(list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer'])))

#c = Counter(list_word[0])
#b = Counter(word)

#print(b==c)


'''
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

спаниель — апельсин
карат — карта — катар
топор — ропот — отпор
src/solution.py

Реализуйте функцию filter_anagrams(), которая находит все слова-анаграммы. Функция принимает исходное слово и последовательность (iterable) слов для проверки, 
а возвращает последовательность анаграмм.

Я использовал в абзаце "слова" только для краткости. Строго говоря, ваша функция должна уметь находить анаграммы любых последовательностей, 
в том числе списков и кортежей. То есть решение должно быть максимально общим.

list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# ['aabb', 'bbaa']
list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# ['carer', 'racer']
list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
# []
list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))
# [[2, 1], [1, 2]]
'''