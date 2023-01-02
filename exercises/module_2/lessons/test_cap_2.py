from capitalize import capitalize

if capitalize('hello') != 'Hello':
    #print('Функция работает неверно!')
    raise Exception('Функция работает неверно!')

elif capitalize('') != '':
    #print('Функция работает неверно!')
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')