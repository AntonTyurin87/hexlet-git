def rgb(red=0, green=0, blue=0):
    return f'rgb({red}, {green}, {blue})'

color = 'red'

def get_colors(color):
    if color == 'red':
        return rgb(255, 0, 0)
    elif color == 'green':
        return rgb(0, 255, 0)
    elif color == 'blue':
        return rgb(0, 0, 255)

#print(get_colors(colors))


colors = get_colors()
set(colors.keys()) == {'red', 'green', 'blue'}

'''
В этом упражнении вам нужно будет, используя функцию rgb(), реализовать функцию get_colors(), 
которая должна вернуть словарь цветов (о цветовой модели RGB вы можете почитать тут). 
В словаре должны присутствовать ключи 'red', 'green', 'blue'. 
Каждому ключу должен соответствовать результат вызова функции rgb() со значением 255 для соответствующего ключу аргумента. 
Для построения каждого цвета используйте только один аргумент!

colors = get_colors()
set(colors.keys()) == {'red', 'green', 'blue'}
# True
colors['red']
# 'rgb(255, 0, 0)'
colors['blue']
# 'rgb(0, 0, 255)'
'''