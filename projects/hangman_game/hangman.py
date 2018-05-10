"""
File: hangman.py
Author: setcain
Email: setcain@gmail.com
Github: https://github.com/setcain
Description: My first game in python
"""

# Imports
import random

# Const
IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
        'lavadora', 'secadora', 'sofa', 'gobierno', 'diputado', 'democracia',
        'computadora', 'teclado'
        ]


def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('+ --- + --- + --- +')


def main():
    word = random_word()
    tries = 0
    hidden_word = ['-'] * len(word)

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Chose a letter: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1

        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

            letter_indexes = []


if __name__ == "__main__":
    print('''
    Welcome to my first game in python
    ''')
    main()
