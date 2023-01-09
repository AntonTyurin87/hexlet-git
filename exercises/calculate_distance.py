from math import sqrt

point1 = [0, 0]
point2 = [3, 4]

def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


print(calculate_distance(point1, point2))


'''
src/points.py
Реализуйте функцию calculate_distance(), которая находит расстояние между двумя точками на плоскости:

point1 = [0, 0]
point2 = [3, 4]
calculate_distance(point1, point2)  # 5.0
Подсказки
Формула расчёта расстояния между двумя точками
'''