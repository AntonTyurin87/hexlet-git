#data = ('foo', [1, 2, 3], '')


def product(arg, *args):  

    if len(args) == 2:
        return [(a,b,d) for a in arg for b in args[0] for d in args[1]]

    return list(zip(arg, *args))

#print(product([0, 1], [2, 3], [4, 5]))

'''

def product(arg, *args):
    c = []
    #if arg == None:
        #return None

    if arg == []:
        return arg
    
    if isinstance(arg, str) and len(args) == 0:
        return [(a,) for a in arg]

    #if len(arg) == 1:
        #return [arg,]

    for i in arg, args:

        if i == c or i == '':
            return c
        
    if len(args) == 2:
        return [(a,b) for a in args[0] for b in args[1]]

    if len(args) == 3:
        return [(a,b,d) for a in args[0] for b in args[1] for d in args[2]]

print(product('A', 'B'))




s1 = [1, 2]
s2 = 'abc'


def decart(s1,s2):
   return [(a,b) for a in s1 for b in s2]

print(decart(s1,s2))

Вам предстоит реализовать функцию product(), которая принимает один и более позиционных параметров — iterable любого вида, 
и возвращает список кортежей. Возвращаемый список представляет собой декартово произведение элементов входных последовательностей — 
все сочетания "каждый с каждым". Например, для последовательностей [1, 2] и 'ab' (помним, строки — тоже iterable) 
функция должна вернуть список [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')], то есть каждый элемент списка с каждым символом строки.

from solution import product
product()  # хотя бы одна последовательность должна быть дана
# Traceback (most recent call last):
#    ...
# TypeError: product() missing 1 required positional argument: 'sequence'
product([])
# []

product([1, 2], 'abc')
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

product('hello', [], 'world')
# []
# ^ если хотя бы одна из входных последовательностей пустая,
# то выходной список тоже будет пуст
'''