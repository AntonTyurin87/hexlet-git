READ_ONLY = 'read_only'
flags = set()


def toggled(READ_ONLY, flags):
    #flags.clear()
    #flags.add(READ_ONLY)
    flags_2 = flags.copy()
    flags_2.add(READ_ONLY)
    return flags_2


new_flags = toggled(READ_ONLY, flags)

print(READ_ONLY in flags)

print(READ_ONLY in new_flags)

'''
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