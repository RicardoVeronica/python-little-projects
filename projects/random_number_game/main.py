"""
File: game
Author: setcain
Email: setcain@email.com
Github: https://github.com/setcain
Description: A simple game in python
Todo: Difficulty of the game
"""

import random


def main():
    tries = 0
    random_number = random.randint(1, 10)

    while tries < 5:
        try:
            user = int(input('''
                ===== Find the number =====
                You only have 5 tries

                write a number: 
                ''')) 

        except ValueError:
            print('Try with a number')

        else:

            if user == random_number:
                print('great')
                break

            else:
                if user < random_number:
                    print('more higher')
                    tries += 1
                    print('Try number: {}'.format(tries))

                elif user > random_number:
                    print('more bottom')
                    tries += 1
                    print('Try number: {}'.format(tries))

    else: 
        print('Game over, try it again')
        ask = input('Do you want to play again? [y/n]')
        if ask == 'y':
            main()
        else:
            print('Ok, see you later')


if __name__ == "__main__":
    main()
