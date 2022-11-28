
def memoized(function):
    dictionary = {}
    def inner(number):
        #a = function
        #print(a)
        if number in dictionary:
            #print(function)
            return dictionary.get(number)
        else:
            result = function(number)
            dictionary.update({number: result})
            return result
    return inner

#from solution import memoized
@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))

print(f(1))

print(f(42))

print(f(42))

print(f(1))

'''
Вам предстоит реализовать декоратор, добавляющий функции мемоизацию. 
Мемоизация — это запоминание уже вычисленных результатов для уже однажды встреченных аргументов.

Для простоты будем считать, что мемоизироваться будут численные функции одного аргумента 
(аргумент — число, результат — тоже число).

from solution import memoized
@memoized
def f(x):
    print('Calculating...')
    return x * 10
 
f(1)
# => Calculating...
# 10
f(1)
# 10
f(42)
# => Calculating...
# 420
f(42)
# 420
f(1)
# 10
Заметьте, что для каждого нового аргумента выводится сообщение "Calculating...", но только лишь один раз.
'''