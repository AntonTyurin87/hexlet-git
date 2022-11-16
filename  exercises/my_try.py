name = 'Bob'

def greet(*args):
    if len(args) != 0:
        phrase = []
        for n in (args,):
            phrase += {n} 

        print('Hello, ' + ' and '.join(phrase) + '!')


greet('Bob')
