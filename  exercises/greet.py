
name = 'Bob'

def greet(name, *args):
    phrase = []
    for n in (name,) + args:
        phrase += {n} 

    return ('Hello, ' + ' and '.join(phrase) + '!')


greet(name)

'''
Вам нужно реализовать функцию greet(), которая должна принимать несколько имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).

greet('Bob')
# 'Hello, Bob!'
greet('Moe', 'Mary')
# 'Hello, Moe and Mary!'
greet(*'ABC')
# 'Hello, A and B and C!'


Подсказки
При решении вам может пригодиться метод join() у объекта строки. Работает он так:
','.join(['A', 'B', 'C'])
# 'A,B,C'
','.join(['A'])
# 'A'
''.join(['Hello', 'World'])
# 'HelloWorld'




        if isinstance(name, list) | len([name]) == 1:
            print('Hello, ' + str(''.join(name)) + '!')
        else:
            phrase = []
            for n in (name,) + args:
                phrase += n 


'''