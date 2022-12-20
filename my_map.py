func = abs

iter = [-1, 2, -3]

n = 3

def my_map(func, iter):
    for i in iter:
        yield func(i)

def my_filter(func, iter):
    for i in iter:
        if func(i):
            yield i

def replicate_each(n, iter):
    for i in iter:
        for j in range(n):
            yield i

print(list(my_map(abs, [-1, 2, -3])))

print(list(my_filter(lambda x: x % 2 == 1, range(10))))

print(list(replicate_each(3, [1, 'a'])))  # [1, 1, 1, 'a', 'a', 'a'])
'''
Вам предстоит потренироваться в написании генераторных функций и написать три штуки:

my_map(f, xs), которая должна работать как упрощенная версия map()
my_filter(f, xs), упрощенный вариант filter()
replicate_each(n, xs) должен для каждого элемента итератора xs выдавать на выход по n копий этого элемента
from solution import my_map, my_filter, replicate_each
list(my_map(abs, [-1, 2, -3]))  # [1, 2, 3]
list(my_filter(lambda x: x % 2 == 1, range(10)))  # [1, 3, 5, 7, 9]
list(replicate_each(1, [1, 'a']))  # [1, 'a']
list(replicate_each(3, [1, 'a']))  # [1, 1, 1, 'a', 'a', 'a']
list(replicate_each(0, [1, 'a']))  # []
Подсказки
Если линтер будет выдавать предупреждение WPS526, то просто игнорируйте его: линтер здесь видит, 
что мы пишем совсем уж тривиальные штуки, хотя должны бы использовать map() и filter() — 
но ведь в этом вся суть упражнения, чтобы их не использовать :
'''