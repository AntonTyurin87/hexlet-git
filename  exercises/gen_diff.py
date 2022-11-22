A = {"one": "eon", "two": "two", "four": True}
B = {"two": "own", "zero": 4, "four": True}

def gen_diff(A, B):
    C = {}
    C.update(A)
    C.update(B)
    for key, value in A.items():
        if key in B.keys() and value in B.values():
            C.update({key: 'unchanged'})
        elif key in B.keys() and value not in B.values():
            C.update({key: 'changed'})
        elif key not in B.keys():
            C.update({key: 'deleted'})

    for key in B:
        if key not in A.keys():
            C.update({key: 'added'})

    return C

print(gen_diff(A, B))


'''
Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает результат сравнения в виде словаря. 
Ключами результирующего словаря будут все ключи из двух входящих, а значением строка с описанием отличий: 
added, deleted, changed или unchanged.

Возможные значения:

added — ключ отсутствовал в первом словаре, но был добавлен во второй
deleted — ключ был в первом словаре, но отсутствует во втором
+++   changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
+++   unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями
Пример работы:

from solution import gen_diff

gen_diff(
    {"one": "eon", "two": "two", "four": True},
    {"two": "own", "zero": 4, "four": True},
)
# {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
'''