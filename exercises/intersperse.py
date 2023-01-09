data = [1, 2, 3, 4, 5]
separator = 0

def intersperse(data, separator):
    data_2 = iter(data)
    n = 0
    while n < len(data)-1:
        yield data_2
        n += 1

a = intersperse(data, separator)

print(next(a))

print(intersperse(data, separator))
print(next(intersperse(data, separator)))
print(next(intersperse(data, separator)))
print(next(intersperse(data, separator)))
print(next(intersperse(data, separator)))





#print(list(intersperse(range(4), 0)))  # [0, 0, 1, 0, 2, 0, 3]

#print("".join(intersperse(["Hello", "World"], " ")))  # 'Hello World'

'''
Вам предстоит реализовать функцию intersperse(), которая должна принимать два аргумента:

Итерируемый источник значений
Значение-разделитель
Функция должна возвращать такой итератор, который отдавал бы значение-разделитель между соседними значениями из источника. Помните, что:

Ваша функция должна возвращать именно итератор
Ни один элемент из входного итератора не должен быть получен, пока это значение не потребуют от результирующего итератора (если вообще потребуют!)
Результирующий итератор не должен вставлять разделитель следом за последним элементом входного потока

from solution import intersperse

list(intersperse([], ","))  # []

list(intersperse([42], "foo"))  # [42]

"".join(intersperse(["Hello", "World"], " "))  # 'Hello World'

list(intersperse(range(4), 0))  # [0, 0, 1, 0, 2, 0, 3]

'''