class Truncater:
    OPTIONS = {
    'separator': '...',
    'length': 200,
}
    def __init__(self, **options):
        Truncater.OPTIONS.update(dict(options))

    def truncate(self, text, **options):

        separator = ''

        if 'separator' in options:
            separator = options['separator']
        else:
            separator = Truncater.OPTIONS['separator']

        if 'length' in options:
            length = options['length']
        else:
            length= Truncater.OPTIONS['length']

        out = ''
        if len(text) > length:
            for i in range(0, length):
                out += text[i]
        else:
            return text

        out += separator

        return out
    

truncater = Truncater()

print(truncater.truncate('one two')) # 'one two'
print(truncater.truncate('one two', length=6)) # 'one tw...'
print(truncater.truncate('one two', separator='.')) # 'one two'
print(truncater.truncate('one two', length=3)) # 'one...'

truncater = Truncater(length=3)

print(truncater.truncate('one two')) # 'one...'
print(truncater.truncate('one two', separator='!')) # 'one!'
print(truncater.truncate('one two')) # 'one...'

print(truncater.truncate('one two', length=7)) # 'one two'

'''
truncater.truncate('one two')  # one two

print(truncater.truncate('one two'))
 
truncater.truncate('one two', length=6)  # one tw...

print(truncater.truncate('one two', length=6))

print(truncater.truncate('one two', separator='.'))
 
truncater2 = Truncater(length=6, separator='*')
truncater2.truncate('one two')  # one tw*

print(truncater2.truncate('one two'))


Реализуйте класс Truncater с единственным методом truncate(). В классе уже присутствует конфигурация по умолчанию:

OPTIONS = {
    'separator': '...',
    'length': 200,
}
separator отвечает за символ(ы) добавляющиеся в конце, после обрезания строки, а length это длина до которой происходит сокращение. 
Если строка короче или равна этой опции, то никакого сокращения не происходит. 
Конфигурацию по умолчанию можно переопределить передав новую при инициализации (она мержится с тем что в классе), 
а также через передачу конфигурации вторым параметром в метод truncate(). Оба этих способа можно комбинировать.

truncater = Truncater()
 
truncater.truncate('one two')  # one two
 
truncater.truncate('one two', length=6)  # one tw...
 
truncater2 = Truncater(length=6, separator='*')
truncater2.truncate('one two')  # one tw*




class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }

    def __init__(self, **options):
        self.options = PasswordValidator.OPTIONS | options

    def validate(self, password):
        errors = {}
        if len(password) < self.options['min_len']:
            errors['min_len'] = 'too small'
        if self.options['contain_numbers']:
            if not self._has_number(password):
                errors['contain_numbers'] = 'should contain at least one number'
        return errors
'''