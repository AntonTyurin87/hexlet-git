from collections import Counter
string = 'rkqodlw'
word = 'World'

def scrabble(string, word):
    return (Counter(word.lower()) - Counter(string.lower()) == Counter())

    print(word)
    print(string)

    print(word in string)

scrabble(string, word)

print(scrabble(string, word))

'''
Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра: набор символов (строку) и слово, 
и проверяет, можно ли из переданного набора составить это слово. В результате вызова функция возвращает True или False.

При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.

Для решения используйте встроенный инструмент — Counter.

Пример
scrabble('rkqodlw', 'world')  # True
scrabble('avj', 'java')  # False
scrabble('avjafff', 'java')  # True
scrabble('', 'hexlet')  # False
scrabble('scriptingjava', 'JavaScript')  # True
'''