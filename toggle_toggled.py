READ_ONLY = 'read_only'
flags = set()

def toggle(READ_ONLY, flags):
    if READ_ONLY in flags:
        flags.discard(READ_ONLY)
    else:
        flags.add(READ_ONLY)


def toggled(READ_ONLY, flags):
    return flags.add(READ_ONLY)


'''
В нашем случае флаги будут представлять собой элементы множества: 
если элемент в множестве присутствует, значит и флаг поднят. 
Вам же нужно будет реализовать две функции: toggle() и toggled().

Функция toggle()
Эта функция должна принимать флаг (один!) и множество в качестве аргументов. 
Если флаг уже присутствует в множестве, его нужно из множества убрать. 
Если же флаг отсутствует, то его нужно добавить. 
Таким образом функция будет переключать состояние флага. 
Множество нужно заменять "по месту", возвращать из функции ничего не нужно. 
Пример использования функции toggle():

READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
READ_ONLY in flags  # True
toggle(READ_ONLY, flags)
READ_ONLY in flags  # False

/////////////////////////////////////////////////////////////////////////////

Функция toggled()
Эта функция работает похожим на toggle() образом, 
но вместо изменения исходного множества возвращает новое — с уже переключенным флагом. 
Пример:

READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
READ_ONLY in flags  # False
READ_ONLY in new_flags  # True
'''