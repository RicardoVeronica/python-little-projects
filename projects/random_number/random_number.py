"""
File: random.py
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: Test module random
"""


# Imports
import random

# Const
INIT = 'Give a number: '
WIN = 'Congratulations you find the number'
LITTLE_THAN = 'The random number is little than this, try again'
BIGGER_THAN = 'The random number is bigger than this, try again'

# Main method
if __name__ == "__main__":
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input(INIT))
        if number == random_number:
            print(WIN)
            number_found = True
        elif number > random_number:
            print(LITTLE_THAN)
        else:
            print(BIGGER_THAN)
