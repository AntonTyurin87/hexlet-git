target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}

def apply_diff(target, diff):
    if 'add' in diff:
        target.update(set(diff.get('add')))
    if 'remove' in diff:
        target.difference_update(set(diff.get('remove')))

apply_diff(target, diff)

print(target)

'''
Цель упражнения — функция apply_diff(). Эта функция принимает два аргумента, первым из которых выступает множество, 
которое нужно будет изменять "по месту" (возвращать ничего не нужно). Вторым аргументом функция принимает словарь, 
который может содержать ключи 'add' и 'remove' с множествами в качестве значений. Значения по ключу 'add' нужно добавить в изменяемое множество, 
а значения по ключу 'remove' — убрать из множества. Прочие ключи в переданном словаре значения не имеют и обрабатываться не должны.

target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
print(target)  # => {'c', 'b'}

Подсказки
Не используйте методы add и discard. В этом упражнении нужно манипулировать множествами "целиком".
'''