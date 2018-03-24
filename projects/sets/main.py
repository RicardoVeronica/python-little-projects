"""
File: game
Author: setcain
Email: setcain@email.com
Github: https://github.com/setcain
Description: simple game
"""

from init import menu 


def main():
    while True:
        play_game = str(input('''
            ===== Do you want to play... [y/n] =====
                              '''))

        if play_game == 'y':
            user_msg = 'You need to write some numbers'

            print('Ok, just write a list of numbers, separete them for a'
                  'space, like: 1 2 3 4 5')
            
            user = set(input('\nWrite the first set here: '))
                    
            if len(user) == 0:
                print(user_msg)

            else:
                user_2 = set(input('Write the second set here: '))

                if len(user_2) == 0:
                    print(user_msg)

                else:
                    menu(user, user_2)

        elif play_game == 'n':
            print('\nOk. See you aroud...')
            break

        else:
            print('\nWrite a valid option')


if __name__ == "__main__":
    main()
