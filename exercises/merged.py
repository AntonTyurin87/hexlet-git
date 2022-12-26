A = [{'a': 1, 'b': 2},
    {'b': 10, 'c': 100},]

A = [{'a': 1}, {'a': 2}, {'a': 3}]


def merged(A):
    C = {}
    
    for i in A:
        C.update(i)

    C = dict.fromkeys(set(C), set())

    for j in A:
        for k in j:
            if C.get(k):
                h.add(j.get(k))

            else:
                h = set()
                h.add(j.get(k))
                print(h)
            C.update({k:h})

    for r in C:
        if type(C.get(r)) != set:
            C.update({r:{C.get(r)}})

    return C

print(merged(A))



#merge(A)

'''
Реализуйте функцию merged(), которая объединяет несколько словарей в один общий словарь. 
Функция принимает список словарей и возвращает результат в виде словаря, в котором каждый ключ содержит множество (set) уникальных значений.

from solution import merged
merged([{}, {}]) == {}
# True
merged([
    {'a': 1, 'b': 2},
    {'b': 10, 'c': 100},
]) == {'a': {1}, 'b': {2, 10}, 'c': {100}}
# True
'''