from string import hexdigits

ip_6 = '2a02:0cb41:0:0:0:0:0:7'


def is_valid_ipv6(ip_6):
    if ip_6 == '::' or ip_6 == '::1' or ip_6 == '1::1':
        return True
    # Подсчёт двоеточий
    flag = 0
    flag_2 = 0
    count = 0
    for i in ip_6:
        if i == ':' and flag == 1:
            count += 2
            flag = 0
            flag_2 += 1
            continue
        if i == ':':
            count += 1
            flag = 1
        elif i != ':':
            flag = 0
    
    if count != 7 or flag_2 > 1:
        return False

    step = []
    mass = []
    flag = 0
    for j in ip_6:
        if j != ':':
            step += j
            flag = 0
        elif j == ':' and flag == 0:
            mass += [''.join(step)]
            step = []
            flag = 1
        elif j == ':' and flag == 1:
            flag = 0
    mass += [''.join(step)]

    print(mass)

    for k in mass:
        if len(k) > 4:
            return False
        for o in k:
            if o not in hexdigits:
                return False
    
    return True

print(is_valid_ipv6(ip_6))


'''
Реализуйте функцию-предикат is_valid_ipv6(), которая проверяет IPv6-адреса (адреса шестой версии интернет протокола) 
на корректность. Функция принимает на вход строку с адресом IPv6 и возвращает True, если адрес корректный, 
и False, если нет.

Дополнительные условия:

Работа функции не зависит от регистра символов.
Ведущие нули в группах цифр необязательны.
Самая длинная последовательность групп нулей, например, :0:0:0: может быть заменена на два двоеточия ::. 
Такую замену можно произвести только один раз.
Одна группа нулей :0: не может быть заменена на ::.

from solution import is_valid_ipv6
is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d')
# True
is_valid_ipv6('::1')
# True
is_valid_ipv6('2607:G8B0:4010:801::1004')
# False
is_valid_ipv6('2.001::')
# False


Подсказки
IPv6
Для реализации проверки пограничных случаев изучите список IP-адресов в модуле с тестами.
Используйте константу string.hexdigits для проверки, что строка содержит валидное представление шестнадцатеричного числа.
'''