number = 1

number_list = [15, 10]

def find_index_of_nearest(number, number_list):
    if number_list == []:
        return None
    delta = []
    for i in number_list:
        delta.append(abs(i-number))
    return delta.index(min(delta))

print(find_index_of_nearest(number, number_list))

'''
Реализуйте функцию find_index_of_nearest(), которая принимает на вход список чисел и искомое число. 
Задача функции — найти в списке ближайшее число к искомому и вернуть его индекс.

Если в списке содержится несколько чисел, одновременно являющихся ближайшими к искомому числу, 
то возвращается наименьший из индексов ближайших чисел.

find_index_of_nearest(2, []) is None
# True
find_index_of_nearest(0, [15, 10, 3, 4])
# 2
find_index_of_nearest(4, [7, 5, 3, 2])
# 1
find_index_of_nearest(4, [7, 5, 4, 4, 3])
# 2
'''