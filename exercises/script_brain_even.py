#!/usr/bin/env python3
from launcher_game import welcome_user, game_launch
from game_even_game import rules, even_game


def main():
    name = welcome_user()
    rules()
    game_launch(even_game, name)
    

if __name__ == '__main__':
    main()