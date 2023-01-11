from point import make_decart_point
from math import sqrt

point1 = make_decart_point(3, 2)
point2 = make_decart_point(0, 0)


def make_segment(point1, point2):
    #segment = sqrt((point2['x'] - point1['x'])**2 + (point2['y'] - point1['y'])**2)
    #return {'x': point2['x'] - point1['x'], 'y': point2['y'] - point1['y']}
    return {'x1': point1['x'], 'x2': point2['x'], 'y1': point1['y'], 'y2': point2['y']}

segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))

def get_mid_point_of_segment(segment):
    return {'x': (segment['x1'] + segment['x2'])/2, 'y': (segment['y1'] + segment['y2'])/2}

def get_begin_point(segment):
    return {'x': segment['x1'], 'y': segment['y1']}

def get_end_point(segment):
    return {'x': segment['x2'], 'y': segment['y2']}

#print(segment)

'''

Отрезок — еще один графический примитив. В коде описывается парой точек, одна из которых — начало отрезка, другая — конец. Обычный отрезок не имеет направления, поэтому вы сами вольны выбирать то, какую точку считать началом, а какую концом.

В этом задании подразумевается, что вы уже понимаете принцип построения абстракции и способны самостоятельно принять решение о том, как она будет реализована. Напомню, что сделать это можно разными способами и нет одного правильного.

src/segments.py
Реализуйте указанные ниже функции:

make_segment() — принимает на вход две точки и возвращает отрезок.
get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку, находящуюся на середине отрезка.
get_begin_point() — принимает на вход отрезок и возвращает точку начала отрезка.
get_end_point() — принимает на вход отрезок и возвращает точку конца отрезка.
Представление отрезка вы должны придумать сами!

Пример работы:

from points import make_decart_point
 
segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
get_begin_point(segment)  # (3, 2)
get_end_point(segment)  # (0, 0)
get_mid_point_of_segment(segment)  # (1.5, 1)
Подсказки
Для создания точек используйте функцию make_decart_point.
'''


