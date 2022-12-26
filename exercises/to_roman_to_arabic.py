number_a = 1999
number_r = 'X'

def to_roman(number_a):
    roma = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roma_number = []
    roma_number += roma.get(1000)*(number_a//1000)
    number_a = number_a%1000
    if number_a >= 900:
         roma_number += roma.get(100)
         roma_number += roma.get(1000)
         number_a = number_a - 900
    roma_number += roma.get(500)*(number_a//500)
    number_a = number_a%500
    if number_a >= 400:
        roma_number += roma.get(100)
        roma_number += roma.get(500)
        number_a = number_a - 400
    roma_number += roma.get(100)*(number_a//100)
    number_a = number_a%100
    if number_a >= 90:
        roma_number += roma.get(10)
        roma_number += roma.get(100)
        number_a = number_a - 90
    roma_number += roma.get(50)*(number_a//50)
    number_a = number_a%50
    if number_a >= 40:
        roma_number += roma.get(10)
        roma_number += roma.get(50)
        number_a = number_a - 40
    roma_number += roma.get(10)*(number_a//10)
    number_a = number_a%10
    if number_a == 1 or number_a == 2 or number_a == 3:
        roma_number += roma.get(1)*number_a
    elif number_a == 4:
        roma_number += roma.get(1)
        roma_number += roma.get(5)
    elif number_a == 5:
        roma_number += roma.get(5)
    elif number_a == 6 or number_a == 7 or number_a == 8:
        roma_number += roma.get(5)
        roma_number += roma.get(1)*(number_a-5)
    elif number_a == 9:
        roma_number += roma.get(1)
        roma_number += roma.get(10)

    return ''.join(roma_number)

def to_arabic(number_r):
    arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    counter_r = 0
    counter_1 = 0
    counter_2 = 0
    counter_w_1 = ''
    counter_w_2 = ''
    arabic_number = []
    number_r_rev = list(number_r)
    for i in reversed(number_r_rev):
        #print(i)
        counter_2 = counter_1; #print(counter_2)
        counter_1 = arabic.get(i); #print(counter_1)
        counter_w_2 = counter_w_1
        counter_w_1 = i

        if counter_2 == counter_1:
            counter_r += 1

        if counter_r > 2:
            return False

        if counter_w_1 == 'V' and counter_w_2 == 'X':
            return False

        if counter_1 >= counter_2:
            arabic_number += [arabic.get(i)]
            #counter_r = 0
        else:
            arabic_number += [- arabic.get(i)]
            
        #print(arabic_number)

    return sum(arabic_number)



print(to_roman(number_a))

print(to_arabic(number_r))

'''

1	    I	лат. unus, unum
5	    V	лат. quinque
10	    X	лат. decem
50	    L	лат. quinquaginta
100	    C	лат. centum
500	    D	лат. quingenti
1000	M	лат. mille

Реализуйте функцию to_roman(), которая переводит арабские числа в римские. Функция принимает на вход целое число из диапазона от 1 до 3000, а возвращает строку с римским представлением этого числа.

Реализуйте функцию to_arabic(), которая переводит число в римской записи в число, записанное арабскими цифрами. Если переданное римское число не корректно, то функция должна вернуть значение False.

Примеры
to_roman(1)  # 'I'
to_roman(59)  # 'LIX'
to_roman(3000)  # 'MMM'
to_arabic('I')  # 1
to_arabic('LIX')  # 59
to_arabic('MMM')  # 3000
to_arabic('IIII')  # False
to_arabic('VX')  # False


Алгоритм 1

1. Выделяем (если есть) количество целых тысяч. Полученное значение позволить сгенерировать строку с n количеством «M» (читаем, n*1000).
Пример: 2012 после первого пункта даст «MM»

2. Получаем остаток после деления на 1000, чтобы выделить в дальнейшем следующие значения.

3. Выделяем (если возможно), целые 500. При этом учитываем что если полученное значение равно 4 (5+4=9), 
то следует записывать как значение 1000-100, что в римский СС равнозначно «CM».
Пример: 1887 после этого пункта даст нам «MD».
1945 соответственно «MCM».

4. Получаем остаток от деления на 500.

5. Делим на 100 чтобы выделить целые сотни и складываем к предыдущему результату. Учитываем что если получили 4, 
что равнозначно 400, то записываем как 500-100, то есть «CD».
Пример: 1709 даст после этого шага «MDCCC».

6. Получаем остаток от деления на 100.

7. Выделяем из него целые пол сотни. Если значение будет равно 4 (то есть 90), то записываем как 100-10, что равно «XC». Иначе прибавляем к строке «L»
Пример: 1986 после всего выдаст нам «MCML».

8. Выделяем остаток от 50.

9. Выделяем целое количество десятков и складываем к строке n раз символ «X». При этом учитываем что 40 пишется как 50-10, то есть «XL».
Пример: 1986 после всего выдаст нам «MCMLXXX».

10. Получаем остаток от деления на 10. Этот шаг отличается от других тем, что можно сразу приравнять остаток к его эквиваленту. 1=I, 7=VII и так далее.

После перебора числа этим алгоритмом мы получаем примерно такое:
2012 == MMXII

'''