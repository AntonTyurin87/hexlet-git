hr_tag = {
  'name': 'hr',
  'class': 'px-3',
  'id': 'myid',
  'tag_type': 'single',
}


def stringify(hr_tag):
    string = ''
    for i in hr_tag:
        if i != 'name' and i != 'tag_type' and i != 'body':
            string += ' ' + str(i) + '=' + '"' + str(hr_tag[i]) + '"'
    print(string)

    if 'body' in hr_tag and hr_tag['tag_type'] == 'pair':
        string = f'<{hr_tag["name"]}{string}'
        string += '>' + hr_tag['body'] 
        string += '</' + str(hr_tag['name']) + '>'
    if hr_tag['name']and hr_tag['tag_type'] == 'single':
        string = f'<{hr_tag["name"]}{string}'
        string += '>'
    if 'body' not in hr_tag and hr_tag['tag_type'] == 'pair':
        string = f'<{hr_tag["name"]}{string}'
        string += '>' + '</' + str(hr_tag['name']) + '>'

    return string


 

print(stringify(hr_tag))






'''
Реализуйте функцию stringify(), которая принимает на вход тег и возвращает его текстовое представление.

from solution import stringify
 
hr_tag = {
  'name': 'hr',
  'class': 'px-3',
  'id': 'myid',
  'tag_type': 'single',
}
html = stringify(hr_tag) ## <hr class="px-3" id="myid">
 
div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': 'text2',
  'id': 'wow',
}
html = stringify(div_tag) ## <div id="wow">text2</div>
 
empty_div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': '',
  'id': 'empty',
}
html = stringify(empty_div_tag) ## <div id="empty"></div>
Примечания
В структуре тега есть три специальных ключа:

name — имя тега
tag_type — тип тега, определяет его парность (pair) или одиночность (single)
body — тело тега, используется для парных тегов. Если у парного тега нет содержимого, то body равно пустой строке ''.
Всё остальное становится атрибутами тега и не зависит от того, парный он или нет.

'''