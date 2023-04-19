data = [2, [3, 5], [[4, 3], 2]]

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

                

print(flatten(data))


print(isinstance(data, list))


'''
Реализуйте функцию flatten(), которая делает плоским вложенный список.

from solution import flatten
flatten([])  # []
flatten([2, [3, 5], [[4, 3], 2]])  # [2, 3, 5, 4, 3, 2]

'''