import prompt

counter = 3 #number of game rounds

def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, '{user_name}'!")
    return user_name


def game_launch(game, name):

    round_counter = 0

    while round_counter < 3:
        answer = game()
        if answer[0] == answer[1]:
            print('Correct!')
            round_counter += 1

        else: 
            print(f"'{answer[0]}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{answer[1]}'.")
            print(f"Let's try again, '{name}'!")
            break

    if round_counter == counter:
        print('Congratulations, ' + str(name) + '!')
