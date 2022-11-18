inputfunc = 31


def call_twice(inputfunc, *args, **kwargs):
    return (inputfunc(*args, **kwargs), inputfunc(*args, **kwargs))

'''
Вам предстоит реализовать функцию call_twice(), которая:

Принимает функцию и произвольный набор аргументов для этой функции
Дважды вызывает переданную функцию с заданными аргументами и возвращает пару значений – результаты двух последовательных вызовов переданной функции. 
Расположение элементов в паре соответствует порядку вызовов функции.
from solution import call_twice
call_twice(input, 'Enter value: ')
Enter value: foo
Enter value: bar
# ('foo', 'bar')
'''