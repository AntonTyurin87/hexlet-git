
value = {"hello": "world", "is": True, "nested": {"count": 5}}

#value = {"hello": "world", "is": True, "nested": 5}



def deep_keys(obj, arr = None):
    if not arr: arr = [] # Список создается один раз, при первом вызове.

    for key, val in obj.items():
        arr.append((key, val))

        if type(val) == dict:
            deep_keys(val, arr) # Передается на заполнение в дальнейшие вызовы...

    return arr

print( deep_keys(value) )

'''
def to_list(value):
    data_list = list(value.items())
    return sorted(data_list, key=lambda point: (point[0]))


print(to_list(value))




def stringify(value, replacer = ' ', spaces_count = 1):
    data = []
    for i in value:
        if type(i.values()) != type({}):
            data.append((str(i), str(i.value())))
        else:
            data.append








def stringify(value, replacer = '|-', spaces_count = 2):
    result_str = '{\n' 
    if type(value) != type({}):
        return str(value)
    
    #spaces_count += 1
    for d in value:
        e = value.get(d)

        result_str += replacer*(spaces_count) + str(d) + ':' + ' ' + stringify(e, replacer, spaces_count*2) + '\n'

    #result_str = result_str  + replacer*(spaces_count-1) + '}'

    return result_str + '}'


print(stringify(value, replacer = '|-', spaces_count = 2))

Реализуйте функцию stringify(), похожую на JSON.stringify(), но со следующими отличиями:

ключи и строковые значения должны быть без кавычек;
строчка (линия) в строке заканчивается самим значением, без запятой.
Синтаксис:

stringify(value[, replacer[, spaces_count]])
Параметры:

value
Значение, преобразуемое в строку.
replacer, необязательный
Строка – отступ для ключа; Значение по умолчанию – один пробел.
spacesCount, необязательный
Число – количество повторов отступа ключа. Значение по умолчанию – 1.
from solution import stringify
 
stringify('hello')  # значение приведено к строке, но не имеет кавычек
# hello
stringify(True)
# True
stringify(5)
# 5
 
data = {"hello": "world", "is": True, "nested": {"count": 5}}
stringify(data)  # то же самое что stringify(data, ' ', 1)
# {
#  hello: world
#  is: True
#  nested: {
#   count: 5
#  }
# }
 
stringify(data, '|-', 2)  # символ, переданный вторым аргументом повторяется столько раз, сколько указано третьим аргументом
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }
Подсказки
чтобы лучше понять как работает JSON.stringify(), запускайте его с разными данными и параметрами в консоли браузера.
проверки в тестах идут от простого к сложному:

проверка на примитивных типах;
проверка на "плоских" данных;
проверка на "вложенных" данных.
реализуйте функцию так же пошагово, проверяя, что изменения для сложных кейсов не сломали более простые;

документация по JSON.stringify на MDN.
'''