
string = "AaBbCcDd"

#print(len(set(string)))

def number_of_unique_letters(string):
    return len(set(x for x in string.lower() if x.isalpha()))

print(number_of_unique_letters(string))

'''
Вам необходимо реализовать функцию number_of_unique_letters(), которая должна подсчитывать количество уникальных букв в строке-аргументе без учёта регистра.

from solution import number_of_unique_letters
number_of_unique_letters("")  # 0
number_of_unique_letters("abc")  # 3
number_of_unique_letters("A-a-a-a-a-a!")  # 1
number_of_unique_letters("\\(O_o)/")  # 1
number_of_unique_letters("AaBbCcDd")  # 4
Подсказки
Вам может пригодиться что-то из этого:

'Hello World!'.lower()  # 'hello world!'
'o_O'.upper()  # 'O_O'
'z'.isalpha()  # True
'_'.isalpha()  # False
'''