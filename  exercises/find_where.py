
books = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
]

find = {'author': 'FooBar', 'year': 2222}

def find_where(books, find):
    flag = False
    for n in books:
        for k in find:
            if find.get(k) == n.get(k):
                flag = True
            else:
                flag = False
        if flag:
            return n
    return None

print(find_where(books, find))

'''
Реализуйте функцию find_where(), которая принимает на вход список книг и поисковый запрос и возвращает первую книгу, 
которая соответствует запросу. Каждая книга в списке — это словарь, содержащий её параметры, поисковый запрос — тоже словарь с параметрами.

Если совпадений не было, то функция должна вернуть None.

books = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
]

find_where(books, {'author': 'Shakespeare', 'year': 1611})
# {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}
'''