
my_list = ([1, 2, 3], [3, 4, 5], [5, 6, 7])

def get_unique(*my_list):
    new_list = []
    for i in my_list:
        for j in i:
            if j not in new_list:
                new_list.append(j)

    return new_list

print(get_unique(*my_list))



'''
Напишите функцию get_unique(), которая принимает произвольное количество списков и возвращает список, 
содержащий все элементы из всех списков, но без повторений.

get_unique([1, 2, 3], [3, 4, 5], [5, 6, 7])  # [1, 2, 3, 4, 5, 6, 7]
'''