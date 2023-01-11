import math

x = 4
y = 8


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }



# BEGIN (write your solution here)

point = make_point(x, y)

def get_x(point):
    return int(point["radius"] * math.cos(point["angle"]))

def get_y(point):
    return int(point["radius"] * math.sin(point["angle"]))

# END

print(get_x(point))

print(get_y(point))

'''
В этой задаче тесты написаны для отрезков, которые в свою очередь используют точки. 
Ваша задача - реализовать интерфейсные функции для работы с точками. 
Внутреннее представление точек должно быть основано на полярной системе координат, хотя интерфейс предполагает работу с декартовой системой (снаружи).

src/points.py
Реализуйте интерфейсные функции точек:

make_point(). Принимает на вход координаты и возвращает точку. Уже реализован.
get_x()
get_y()
x = 4
y = 8
 
# point хранит в себе данные в полярной системе координат
point = make_point(x, y)
 
# Здесь происходит преобразование из полярной в декартову
get_x(point)  # 4
get_y(point)  # 8
Подсказки
Трансляция декартовых координат в полярные была описана в теории
Получить x можно по формуле radius * cos(angle)
Получить y можно по формуле radius * sin(angle)
'''