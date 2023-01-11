point1 = {'x': 0, 'y': 0}
point2 = {'x': 4, 'y': 4}

def get_mid_point(point1, point2):
    return {'x': (point1.get('x') + (point2.get('x')))/2, 'y': (point1.get('y') + (point2.get('y')))/2}

print(get_mid_point(point1, point2))