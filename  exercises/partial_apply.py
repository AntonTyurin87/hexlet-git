def greet(name, surname):
    return f'Hello, {name} {surname}!'

name = 'ww'

def partial_apply(name):

    def greet(name, surname):
        return f'Hello, {name} {surname}!'
    return greet

def flip(greet):
    pass


f = partial_apply('Dorian')
print(f)
print(f('Grey'))

'''
В этом упражнении вам нужно будет реализовать две функции высшего порядка, 
возвращающие замыкания: partial_apply() и flip().

partial_apply() принимает функцию от двух аргументов и первый аргумент для неё, 
а возвращает замыкание — функцию, которая примет второй аргумент и наконец применит замкнутую функцию 
к обоим аргументам (и вернёт результат).

def greet(name, surname):
    return f'Hello, {name} {surname}!'
 
f = partial_apply(greet, 'Dorian')
f('Grey')
# 'Hello, Dorian Grey!'

////////////////////////////////////////////////////

Функция flip() принимает в качестве единственного аргумента функцию от двух аргументов. 
Возвращаемое замыкание должно также принять два аргумента, а затем применить к ним замкнутую функцию, 
но аргументы подставить в обратном порядке. Таким образом flip() 
как бы "переворачивает" ("flips") исходную функцию.

def greet(name, surname):
    return f'Hello, {name} {surname}!'
 
f = flip(greet)
f('Christian', 'Teodor')
# 'Hello, Teodor Christian!
'''