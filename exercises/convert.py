data = [
        ['key4', 'value4'],
        ['anotherKey', [
            ['key7', False],
            ['innerKey', []],
        ],
        ],
        ['key6', None],
        ['anotherKey2', [
            ['wow', [['one', 'two'], ['three', 'four']]],
            ['key5', True],
        ],
        ],
    ]

def convert(data):
    data_2 = {}

    for i in data:
        #print(i)
        #print(data_2)
        if isinstance(i[1], str) or isinstance(i[1], bool) or i[1] == None:
            data_2.update({i[0]: i[1]})
        else:
            data_2.update({i[0]: convert(i[1])})

    return data_2


#print(data[1][1])

print(convert(data))

#print(len(data[0][1]))



'''
def convert(data):
    data_2 = {}

    def data_e(b):
        return {b[0]: b[1]}

    def data_d(a):
        if isinstance(a[1], str) or isinstance(a[1], bool):
            return {a[0]: a[1]}
        elif (isinstance(a[1], list) or isinstance(a[1], tuple)) and len(a[1]) > 1:
            f = a[1]
            return {a[0]: data_d(f)}

        elif (isinstance(a[1], list) or isinstance(a[1], tuple)) and len(a[1]) == 1:
            return {a[0]: data_e(a[1])}
        else:
            return {'n': 'n'}

    for i in data:
        data_2.update(data_d(i))
        print(data_2)

    return data_2



Реализуйте функцию convert(), которая принимает на вход список определённой структуры и возвращает словарь, полученный из этого списка.

Список устроен таким образом, что с помощью него можно представлять словари. 
Каждый элемент списка — тоже список из двух элементов, где первый элемент — ключ, а второй — значение. 
Значение тоже может быть списком. Любой список внутри исходного списка всегда рассматривается как данные, 
которые нужно конвертировать в словарь.

from solution import convert
convert([])
# {}
convert([('key2', 'value2'), ('key', 'value')])
# {'key2': 'value2', 'key': 'value'}
convert([
  ('key', [('key2', 'anotherValue')]),
  ('key2', 'value2')
])
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}


def flatten(data):
    data_2 = []

    def data_d(i):
        for j in i:
            if not isinstance(j, list):
                data_2.append(j)
            else:
                data_d(j)

    for i in data:
        if not isinstance(i, list):
            data_2.append(i)
        else:
            data_d(i)



    return data_2
'''