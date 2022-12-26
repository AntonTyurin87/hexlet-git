
spis = [1, 2, 3] 
para_1 = 1
para_2 = 10
spis_2 = [1, 2]

n = 0
k = []
p = []

def length(spis):
    global n
    a = []
    if spis == []:
        a = n
        n = 0 
        return a
    spis.remove(spis[0])
    n +=1
    return length(spis)

def reverse_range(para_1, para_2):
    a = []
    if para_2 == para_1:
        k.append(para_2)
        a.extend(k)
        k.clear()
        return a
    k.append(para_2)
    para_2 -= 1
    return reverse_range(para_1, para_2)


def filter_positive(spis_2):
    a = []
    if spis_2 == []:
        a.extend(p)
        p.clear()
        return a
    if spis_2[0] > 0:
        if spis_2[0] not in p:
            p.append(spis_2[0])
        spis_2.remove(spis_2[0])
    else:
        spis_2.remove(spis_2[0])
    return filter_positive(spis_2)


print(length(spis))

print(reverse_range(para_1, para_2))

print(filter_positive(spis_2))
'''
Привычные нам структуры можно представить и как рекурсивные. 
Например, у списка, есть голова (первый элемент) и хвост (последущие), 
у хвоста тоже есть своя голова и хвост, который тоже можно разделить на голову и хвост. 
И так далее до конца, где последний элемент списка можно представить как голова плюс хвост из пустого списка. 
А вот уже пустой список невозможно разделить, и наша рекурсия остановится.

[1, 2, 3] # голова [1], хвост [2, 3]
[2, 3] # голова [2], хвост [3]
[3] # голова [3], хвост пустой список []
[] # остановка
В этом упражнении вам нужно будет реализовать три несложные функции, но через рекурсивный процесс:

length() принимает список и возвращает его длину
length([1, 2, 3]) # 3

reverse_range() принимает два числа begin и end и возвращает перевернутый список всех чисел между. Для простоты договоримся, что begin <= end
reverse_range(1, 1) # [1]
reverse_range(1, 3) # [3, 2, 1]

filter_positive() принимает список чисел и возвращает новый только с положительными элементами
filter_positive([]) # []
filter_positive([-3]) # []
filter_positive([1, -2, 3]) # [1, 3]

Вы, конечно, можете реализовать функции привычным итеративным способом, но попробуйте сменить угол зрения.
'''