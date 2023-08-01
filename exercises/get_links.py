tags = [
  { 'name': 'img', 'src': 'hexlet.io/assets/logo.png' },
  { 'name': 'div' },
  { 'name': 'link', 'href': 'hexlet.io/assets/style.css' },
  { 'name': 'h1' },
]

def get_links(tags):
    result = []
    for i in tags:
        if i['name'] == 'img':
            result.append(i['src'])
        elif i['name'] == 'a':
            result.append(i['href'])
        elif i['name'] == 'link':
            result.append(i['href'])
    return result

print(get_links(tags))


'''
Реализуйте функцию get_links(), которая принимает на вход список тегов, находит среди них теги a, link и img, а затем извлекает ссылки и возвращает список ссылок. 
Теги подаются на вход в виде списка, где каждый элемент это тег. Тег имеет следующую структуру:

name — имя тега.
href или src — атрибуты. Атрибуты зависят от тега: тег img имеет атрибут src, тег a — href, link — href.
Примеры
from solution import get_links
 
tags = [
  { 'name': 'img', 'src': 'hexlet.io/assets/logo.png' },
  { 'name': 'div' },
  { 'name': 'link', 'href': 'hexlet.io/assets/style.css' },
  { 'name': 'h1' },
]
 
links = get_links(tags)
## [
##   'hexlet.io/assets/logo.png',
##   'hexlet.io/assets/style.css'
## ]
'''