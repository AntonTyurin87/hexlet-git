data = [5, 10, -5, -3, 7]

def barchart(data):

    # положительная полудиаграмма
    mat_posit = []
    count_p = 0
    mat_p = []

    for j in range(max(data)):
        for i in range(len(data)):
            if data[i] > 0 and data[i] > count_p:
                mat_posit += '*'
            else:
                mat_posit += ' '
        count_p += 1

    for x in range(0, len(mat_posit), len(data)):
        mat_p += [''.join(mat_posit[x : len(data) + x])]

    mat_p.reverse()

    # отрицательная полудиаграмма
    mat_neg = []
    count_n = 0
    mat_n = []

    for j in range(abs(min(data))):
        for i in range(len(data)):
            if data[i] < 0 and data[i] < count_n:
                mat_neg += '#'
            else:
                mat_neg += ' '
        count_n -= 1

    for x in range(0, len(mat_neg), len(data)):
        mat_n += [''.join(mat_neg[x : len(data) + x])]


    diog = []
    diog = '\n'.join(mat_p) +'\n' + '\n'.join(mat_n)

    return diog

print(barchart(data))

'''
Реализуйте функцию, которая выводит на экран столбчатую диаграмму. 
Функция принимает в качестве параметра последовательность чисел, 
длина которой равна количеству столбцов диаграммы. Размер диаграммы по вертикали должен определяться 
входными данными.

print(barchart([5, 10, -5, -3, 7]))
# =>  *   
#     *   
#     *   
#     *  *
#     *  *
#    **  *
#    **  *
#    **  *
#    **  *
#    **  *
#      ## 
#      ## 
#      ## 
#      #  
#      #  

print(barchart([5, -2, 10, 6, 1, 2, 6, 4, 8, 1, -1, 7, 3, -5, 5]))
# =>   *            
#      *            
#      *     *      
#      *     *  *   
#      **  * *  *   
#    * **  * *  *  *
#    * **  ***  *  *
#    * **  ***  ** *
#    * ** ****  ** *
#    * ******** ** *
#     #        #  # 
#     #           # 
#                 # 
#                 # 
#                 # 
'''