my_list = [2, 0, 1, -3, 10, -2]

def same_parity_filter(my_list):
    my_list_2 = []
    if my_list == []:
        return my_list_2
    if my_list[0]%2 == 0:
        for i in my_list:
            if i%2 == 0:
                my_list_2.append(i)
    else:
        for i in my_list:
            if i%2 != 0:
                my_list_2.append(i)

    return my_list_2

print(same_parity_filter(my_list))

'''
Реализуйте функцию same_parity_filter(), которая принимает на вход список и возвращает новый список, 
состоящий из элементов, у которых такая же чётность, как и у первого элемента исходного списка.

same_parity_filter([])
# []
same_parity_filter([2, 0, 1, -3, 10, -2])
# [2, 0, 10, -2]
same_parity_filter([-1, 0, 1, -3, 10, -2])
# [-1, 1, -3]
'''