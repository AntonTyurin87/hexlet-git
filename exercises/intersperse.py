itera = range(1, 5)

separator = 0


def intersperse(itera, separator):
    a = 0
    b = itera
    while a < len(itera):
        yield b[a]
        a += 1

'''
    def iterate(x0, m):
    x = x0
    a = 0
    while a < 4:
        yield x  # вместо print()
        a += 1
        x *= m

        intersperse = []
    for i in itera:
            intersperse.append(i)
            intersperse.append(separator)
    intersperse.pop()

'''

print(list(intersperse(itera, separator)))

print(next(intersperse(itera, separator)))
print(next(intersperse(itera, separator)))
print(next(intersperse(itera, separator)))
#print(next(intersperse(itera, separator)))
#print(next(intersperse(itera, separator)))