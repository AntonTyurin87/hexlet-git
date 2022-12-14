data  = '|¯|___|¯¯¯¯¯|___|¯|_|¯' # '110010000100111'

def decode(data):
    bitt = []
    tic = 0
    for i in data:
        if tic == 1:
            bitt += ['1']
            tic = 0
            continue
        if i == '|':
            tic = 1
            continue
        bitt += ['0']
 

    return ''.join(bitt)

print(decode(data))


'''
NRZI код (Non Return to Zero Invertive) — один из способов линейного кодирования. 
Обладает двумя уровнями сигнала и используется для передачи битовых последовательностей, 
содержащих только 0 и 1. NRZI применяется, например, в оптических кабелях, 
где устойчиво распознаются только два состояния сигнала — свет и темнота.

Принцип кодирования

При передаче логического нуля на вход кодирующего устройства передается потенциал, 
установленный на предыдущем такте (то есть состояние потенциала не меняется), 
а при передаче логической единицы потенциал инвертируется на противоположный.

nrzi

src/solution.py`
Реализуйте функцию decode(), которая принимает cтроку в виде графического представления линейного сигнала 
и возвращает строку с бинарным кодом.

decode('_|¯|____|¯|__|¯¯¯')
# '011000110100'
decode('|¯|___|¯¯¯¯¯|___|¯|_|¯')
# '110010000100111'
decode('¯|___|¯¯¯¯¯|___|¯|_|¯')
# '010010000100111'

Подсказки
Символ | в строке указывает на переключение сигнала и означает, что уровень сигнала в следующем такте, будет изменён на противоположный по сравнению с предыдущим.
Если вам нужно будет склеить список строк в одну, воспользуйтесь конструкцией ''.join(list_of_strings) (работает с любым итератором).
'''