
foo = [1, 2, 3]
bar = "abc"
# функция f здеcь та же, что и в первом разделе урока



def f(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

print(f(kx=42, *foo, ky=100, *bar))

'''
    f(kx=42, *foo, ky=100, *bar)
    # (1, 2, (3, 'a', 'b', 'c'), 42, 100, {})
'''