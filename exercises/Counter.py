class Counter:
    value = 0

    def inc(self, delta = 1):
        self.value += delta

    def dec(self, delta = 1):
        self.value -= delta

c = Counter()
c.inc()
c.inc()
c.inc(40)
c.value

'''
class Person:
    name = 'Noname'
    def greet(self):
        print('Hello, ' + self.name + '!')

bob = Person()
bob.name = 'Bob'
bob.greet()
# => Hello, Bob!
alice = Person()
alice.greet()
# => Hello, Noname!

Реализуйте класс Counter, представляющий собой счётчик, хранящий неотрицательное целочисленное значение и позволяющий это значение изменять:

атрибут value должен хранить текущее значение счётчика (вначале равное нулю)
метод inc() должен увеличивать текущее значение на delta единиц (на 1 по умолчанию)
метод dec() должен уменьшать текущее значение на delta единиц (на 1 по умолчанию)
c = Counter()
c.inc()
c.inc()
c.inc(40)
c.value  # 42
c.dec()
c.dec(30)
c.value  # 11
c.dec(delta=100)
c.value  # 0


'''