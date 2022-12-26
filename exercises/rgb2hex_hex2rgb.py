
r = 36
g = 171
b = 0

collor_input = '#24ab00'


def rgb2hex(r=0, g=0, b=0):
    collors_dick = {0: '0', 1 : '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    collor_16 = ['#'] + [collors_dick.get(r//16)] + [collors_dick.get(r%16)] + [collors_dick.get(g//16)] + [collors_dick.get(g%16)] + [collors_dick.get(b//16)] + [collors_dick.get(b%16)]
    return ''.join(collor_16)

#print(rgb2hex(r=36, g=171, b=0))

def hex2rgb(collor_input):
    collors_dick = {'0': 0, '1' : 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    collor_input = list(collor_input)

    collor_res = {}

    def get_collor_number(collor_input):
        return collors_dick.get(collor_input.pop()) + collors_dick.get(collor_input.pop())*16

    collor_res.update({'b': get_collor_number(collor_input)})
    collor_res.update({'g': get_collor_number(collor_input)})
    collor_res.update({'r': get_collor_number(collor_input)})
    
    return collor_res

print(hex2rgb(collor_input))
'''
Для задания цветов в HTML и CSS используются числа в шестнадцатеричной системе счисления. 
Чтобы не возникало путаницы в определении системы счисления, перед шестнадцатеричным числом ставят символ решетки #,
например, #135278. Обозначение цвета (rrggbb) разбивается на три составляющие, 
где первые два символа обозначают красную компоненту цвета, два средних — зеленую, 
а два последних — синюю. Таким образом каждый из трех цветов — красный, зеленый и синий — может принимать значения
от 00 до FF в шестнадцатеричной системе исчисления.

src/Solution.py
При работе с цветами часто нужно получить отдельные значения красного, зеленого и синего (RGB) компонентов цвета 
в десятичной системе исчисления и наоборот. Реализуйте функции rgb2hex() и hex2rgb(), 
которые конвертируют цвета в соответствующие представления цвета.

Функция rgb2hex() принимает 3 параметра (цветные компоненты) и возвращает строку. 
Функция должна работать как с позиционными, так и с именованными аргументами.

Функция hex2rgb() возвращает словарь со значениями компонентов.

Примеры работы:

from solution import hex2rgb, rgb2hex

rgb2hex(36, 171, 0)
# '#24ab00'
rgb2hex(r=36, g=171, b=0)
# '#24ab00'

hex2rgb('#24ab00')
# {'r': 36, 'g': 171, 'b': 0}
'''