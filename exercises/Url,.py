from urllib.parse import urlparse, parse_qs


class Url:

    def __init__(self, url): # принимает на вход HTTP адрес в виде строки.
        self.url = url 


    def get_scheme(self): # возвращает протокол передачи данных.
        a = urlparse(self.url)
        return a.scheme


    def get_hostname(self): # возвращает имя хоста.
        a = urlparse(self.url)
        return a.hostname


    def get_query_params(self): # возвращает параметры запроса в виде пар ключ-значение объекта.
        a = urlparse(self.url)
        b = parse_qs(a.query)
        return b

    def get_query_param(self, k_1, k_2 = None):  # получает значение параметра запроса по имени. Если параметр с переданным именем не существует, 
        a = urlparse(self.url)
        b = parse_qs(a.query)                  # метод возвращает значение заданное вторым параметром (по умолчанию равно None).
        if k_1 in b:
            return b[k_1][0]
        else:
            return k_2


    def __eq__(self, other): # сравнивает два объекта класса Url и возвращает результат сравнения — True или False.
        return self.url == other


url = Url('http://hexlet.io:80?key=value&key2=value2')
print(url.get_scheme())
print(url.get_hostname())
print(url.get_query_params())
print(url.get_query_param('key'))

print(url.get_query_param('key2', 'lala'))
print(url.get_query_param('new', 'ehu'))
print(url.get_query_param('new'))
'''
url = urlparse('http://hexlet.io:80?key=value&key2=value2')
query_string = 'key=value&key2=value2'

a = parse_qs(query_string)

print(a)

print(url)



В данном упражнении вам предстоит реализовать класс Url, который позволяет извлекать из HTTP адреса, представленного строкой, его части.

Класс должен содержать методы:

__init__ — принимает на вход HTTP адрес в виде строки.

get_scheme() — возвращает протокол передачи данных.

get_hostname() — возвращает имя хоста.

get_query_params() — возвращает параметры запроса в виде пар ключ-значение объекта.

get_query_param() — получает значение параметра запроса по имени. Если параметр с переданным именем не существует, 
метод возвращает значение заданное вторым параметром (по умолчанию равно None).

__eq__(self, other) — сравнивает два объекта класса Url и возвращает результат сравнения — True или False.

url = Url('http://hexlet.io:80?key=value&key2=value2')
url.get_scheme() # http
url.get_hostname() # hexlet.io
url.get_query_params()
# {
#  key: [value],
#  key2: [value2],
# }
url.get_query_param('key') # value
# второй параметр — значение по умолчанию
url.get_query_param('key2', 'lala') # value2
url.get_query_param('new', 'ehu') # ehu
url.get_query_param('new') # None
url == Url('http://hexlet.io:80?key=value&key2=value2')) # True
url == Url('http://hexlet.io:80?key=value')) # False
Подсказки
для парсинга url воспользуйтесь функциями urlparse и parse_qs из модуля urllib
__eq__
'''