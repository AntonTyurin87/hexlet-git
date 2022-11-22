from collections import Counter

money = (
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)

def visualize(coins,bar_char='₽'):
    CC = sorted(dict(Counter(coins)).items())
    keys = []
    values = []
    for i in CC:
        keys.append(i[0])
        values.append(i[1])

    stroka_00 = ['# =>',]
    for j in keys:
        if len(str(j)) == 1:
            stroka_00.append(' ' + str(j) + ' ')
        elif len(str(j)) == 2:
            stroka_00.append(' ' + str(j))
    stroka_00.append('\n')

    stroka_01 = ['# => ',]
    stroka_01.append('---'*(len(values)-1))
    stroka_01.append('--' + '\n')

    stroka_02 = ['# => ',]
    stroka_02.append((bar_char*2 + ' ')*(len(values)-1))
    stroka_02.append(bar_char*2 + '\n')

    ind_values = [] #индексы от количества монет

    stroka_j = []

    for k in values:
        stroka_i = ['   ']*(len(values)+2)
        stroka_i[0] = '# =>'
        if max(values) == 0:
            stroka_j += stroka_02
            break
        ma = max(values)
        ind_ma = values.index(max(values))
        values[ind_ma] = 0

        if len(str(ma)) == 1:
            stroka_i[ind_ma + 1] = ' ' + str(ma) + ' '
        elif len(str(ma)) == 2:
            stroka_i[ind_ma + 1] = ' ' + str(ma)

        for r in ind_values:
            stroka_i[r] = ' ' + bar_char*2 

        ind_values.append(ind_ma+1)

        new_ma = max(values)
        
        if new_ma == ma:
            ind_ma = values.index(max(values))
            values[ind_ma] = 0
            if len(str(new_ma)) == 1:
                stroka_i[ind_ma + 1] = ' ' + str(ma) + ' '
            elif len(str(new_ma)) == 2:
                stroka_i[ind_ma + 1] = ' ' + str(ma)
            ind_values.append(ind_ma+1)
            
        
        stroka_i[len(values)+1] = '\n'

        stroka_j += stroka_i


    rez = ''.join(stroka_j) + ''.join(stroka_02) + ''.join(stroka_01)  + ''.join(stroka_00)

    return rez

   
print(visualize(money,bar_char='₽'))

#print(visualize(money,bar_char='₽'))




'''
Реализуйте функцию visualize(), которая подсчитывает сколько монет каждого номинала есть в копилке и показывает результат в виде графика. 
Каждый столбец графика — стопка монет опредлённого номинала.

Для простоты условимся, что монеты в копилке всегда есть, и их количество не ограничено, а номинал может быть любым.

Функция принимает на вход список или кортеж с числами и возвращает график в виде строки. Необязательный аргумент bar_char определяет символ, 
с помощью которого рисуется график. Значение по умолчанию — знак рубля (₽).

Для решения используйте встроенный инструмент — Counter.

from solution import visualize
print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)))
# => 5
# => ₽₽ 4  4
# => ₽₽ ₽₽ ₽₽    3
# => ₽₽ ₽₽ ₽₽    ₽₽
# => ₽₽ ₽₽ ₽₽ 1  ₽₽
# => ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# => --------------
# => 1  2  3  10 20
print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3), bar_char='$'))
# => 5
# => $$ 4  4
# => $$ $$ $$    3
# => $$ $$ $$    $$
# => $$ $$ $$ 1  $$
# => $$ $$ $$ $$ $$
# => --------------
# => 1  2  3  10 20
'''