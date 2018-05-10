"""
File: palindrome_word.py
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: know if a word give it for the user is palindrome
"""


def run():
    word = str(input('Write a word: '))

    if word == word[::-1]:
        print('This word is a palindrome')
    else:
        print('This word is not a palindrome')


if __name__ == '__main__':
    run()
