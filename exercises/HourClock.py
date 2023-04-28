
class HourClock():
    def __init__(self, hour=0):
        self.hour = hour%12

    @hours.setter
    def hours(self, new):
        self.hour = (hour + new)%12


'''
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    # сеттер для свойства full_name
    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')


Реализуйте класс HourClock, который будет изображать часы с одной лишь часовой стрелкой. 
Текущее время (час) должно сообщать свойство hours. Это же свойство должно позволять изменять положение часовой стрелки (посредством сеттера). 
При изменении положения стрелки нужно контролировать, чтобы значение оставалось в диапазоне 0..11 (часов).

clock = HourClock()
clock.hours  # 0
# в начале часовая стрелка всегда на нуле
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 5
clock.hours  # 10
clock.hours += 5
clock.hours  # 3
clock.hours -= 4
clock.hours  # 11
clock.hours = 123
clock.hours  # 3


Подсказки
Используйте модульную арифметику
'''