#!/usr/bin/env python3
import random
import prompt

def rules():
    print('''Answer "yes" if the number is even, otherwise answer "no".''')


# The functionality of the game "Even-Game"
def even_game():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    your_answer = prompt.string('Your answer: ')

    if number % 2 == 0:
        correct_answer = 'yes'
    elif number % 2 != 0:
        correct_answer = 'no'

    return your_answer, correct_answer
