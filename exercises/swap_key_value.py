from my_try import InMemoryKV
import copy


map = InMemoryKV({'key': 10})
map.set_('key2', 'value2')



def swap_key_value(map):
    dict_swap = map.to_dict()
    a = []

    for i in dict_swap:
        a.append((dict_swap[i], i))
        map.unset_(i)

    for j in a:
        map.set_(j[0], j[1])


swap_key_value(map)

print(map.get_('key'))
print(map.get_(10))

map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})

print(map.to_dict())


swap_key_value(map)

print(map.to_dict()) #{'bar': 'foo', 'zoo': 'bar'}