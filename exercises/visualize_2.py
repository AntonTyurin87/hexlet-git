#копилка.py
#kopilka = (10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)

coins = (10,10,1,1,1,1,20,20,20,20,20,2,2,2,2,2,2,3,3,5,5)

def visualize(coins, bar_char='₽'):

    unic_coin = sorted(set(coins))

    k = []
    for j in range(len(unic_coin)):
        k.append([unic_coin[j], 0])

    #print(k)

    for a in range(len(unic_coin)):
       for i in coins:
            if unic_coin[a] == i:
                k[a][1] += 1
    
    counter = []
    for b in range(len(unic_coin)):
        counter.append(k[b][1])

    counter_2 = []
    for b in range(len(unic_coin)):
        counter_2.append(k[b][1])

    string = []

    stroka_0 = ([bar_char*2 + ' ']*len(unic_coin) + ['\n']) # stroka_0 = ([bar_char*2 + ' ']*len(unic_coin) + ['\n'])
    stroka_1 = (['--']*len(unic_coin) + ['-']*(len(unic_coin)-1) + ['\n']) # stroka_1 = (['--']*len(unic_coin) + ['-']*(len(unic_coin)-1) + ['\n'])
    stroka_2 = list(unic_coin)

    stroka_22 = []
    for z in stroka_2:
        if len(str(z)) == 1: 
            stroka_22 = stroka_22 + [str(z) + '  ']
        else:
            stroka_22 = stroka_22 + [str(z) + ' ']
    stroka_22[-1] = stroka_22[-1][0:2]

    #print(stroka_22[-1])

    string_osn = []
    for r in range(len(unic_coin)):
        string_osn.append(['   ']*(len(unic_coin)-1) + ['  '] + ['\n']) # string_osn.append(['   ']*(len(unic_coin)-1) + ['  '] + ['\n'])

    h = 0
    maximum = []

    max_z = 0
    
    for j in range(len(unic_coin)):
        if counter == []:
            break
        maximum = [i for i, v in enumerate(counter_2) if v == max(counter)]
        if max(counter) + 1 < max_z:
            h +=1
        for p in maximum:
            if len(str(counter_2[p])) == 1:
                string_osn[h][p] = str(counter_2[p]) + '  '
            elif len(str(counter_2[p])) == 2:
                string_osn[h][p] = str(counter_2[p]) + ' '
            for y in range(h+1, len(unic_coin)):
                string_osn[y][p] = bar_char*2 + ' '
            max_z = max(counter)
            counter.remove(counter_2[p])

        h +=1
    

    #print(string_osn)

    for u in string_osn:
        u[5] = u[5][0]+u[5][1]
        string += list(u)

    stroka_0[5] = bar_char*2

    Ss = ''.join(string) + ''.join(stroka_0) + ''.join(stroka_1) + ''.join(stroka_22)

    #print(list(Ss))

    #print(list(stroka_0))

    return Ss


print(visualize(coins, bar_char='₽'))

'''

Решение в задание!

    counts = Counter(coins)
    nominals = sorted(counts.keys())
    highest_stack = max(counts.values())

    rows = []
    delimiter = ''

    for level in range(highest_stack, -1, -1):
        row = ''
        for _, bar in sorted(counts.items()):
            if bar > level:
                row += f'{bar_char * 2} '
            elif bar == level and bar != 0:
                row += f'{bar:<2d} '
                delimiter += '---'
            else:
                row += '   '
        rows.append(row[:-1])

    rows.append(delimiter[:-1])
    row = ''
    for nominal in nominals:
        row += f'{nominal:<2d} '
    rows.append(row[:-1])

    return '\n'.join(rows)

'''