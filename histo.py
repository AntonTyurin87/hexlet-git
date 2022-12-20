#a = 1
#b = 6
import random
from collections import Counter

number = 100

def roll_die():
    return random.randint(1, 6)

def histo(rounds_count, roll_die):
    """Draws a horizontal histogram."""
    # BEGIN (write your solution here)
    s = []
    for i in range(rounds_count):
        roll = roll_die()
        if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6:
            s.append(roll)
        else:
            return None

    cnt = Counter(s)

    str_0 = ''

    for k in range(1,7):
        if cnt.get(k):
            str_0 += str(k) +'|' + '#'*cnt.get(k, 0) + ' ' + str(cnt.get(k, ''))
        else:
            str_0 += str(k) +'|'
        if k != 6:
            str_0 += '\n'

    #str_1 = '1|' + '#'*cnt.get(1, 0) + ' ' + str(cnt.get(1, '')) + '\n'
    #str_2 = '2|' + '#'*cnt.get(2, 0) + ' ' + str(cnt.get(2, '')) + '\n'
    #str_3 = '3|' + '#'*cnt.get(3, 0) + ' ' + str(cnt.get(3, '')) + '\n'
    #str_4 = '4|' + '#'*cnt.get(4, 0) + ' ' + str(cnt.get(4, '')) + '\n'
    #str_5 = '5|' + '#'*cnt.get(5, 0) + ' ' + str(cnt.get(5, '')) + '\n'
    #str_6 = '6|' + '#'*cnt.get(6, 0) + ' ' + str(cnt.get(6, ''))

    print(str_0)

histo(10, roll_die)

#print(histo(number, roll_die))

#print(histo(10, roll_die))



'''
Реализуйте функцию histo(), которая выводит на экран горизонтальную гистограмму. 
Функция принимает на вход количество бросков кубика и функцию, которая имитирует бросок игральной кости 
(её реализовывать не нужно). Вызов этой функции генерирует значение от 1 до 6, 
что соответствует одной из граней игральной кости.

Гистограмма содержит строки, каждой из которых соответствует грань игральной кости и количество выпадений 
этой грани. Результаты отображаются графически (с помощью символов #) и в виде числового значения, 
за исключением случаев, когда количество равно 0 (нулю).

Для решения используйте встроенный инструмент — Counter.

roll_die() # 5

print(histo(10, roll_die))
## => 1|###### 6
## => 2|
## => 3|
## => 4|# 1
## => 5|# 1
## => 6|## 2

print(histo(100, roll_die))
## => 1|
## => 2|## 2
## => 3|# 1
## => 4|## 2
## => 5|#### 4
## => 6|#### 4
'''