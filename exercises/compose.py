x = 1

def add5(x):
    return x + 5

def mul3(x):
    return x * 3

def compose(mul3, add5):
    def inner(x):
        return(mul3(add5(x)))
    return inner

#print(compose(mul3, add5, x))

f = compose(mul3, add5)(1)
print(f)

'''
С точки зрения математики, композиция функций f и g — новая функция z(x) = f(g(x)).

src/solution.py
Реализуйте функцию compose(), которая принимает на вход две других одноаргументных функции 
и возвращает новую функцию. Эта новая функция также должна принимать один аргумент и применять к нему исходные функции в нужном порядке: 
для функций f и g порядок применения должен выглядеть, как f(g(x)).

Примеры ниже помогут понять, как должна работать функция:

def add5(x):
    return x + 5

def mul3(x):
    return x * 3

compose(mul3, add5)(1)
# 18
compose(add5, mul3)(1)
# 8
compose(mul3, str)(1)
# '111'
compose(str, mul3)(1)
# '3'
'''