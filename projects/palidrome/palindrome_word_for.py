"""
File: palindrome_word_for.py
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: Know if a word is a palindrome whit a for loop
"""


def palindrome_word_for(word):
    reverse_letters = []

    for letter in word:
        reverse_letters.insert(0, letter)

    reverse_word = ''.join(reverse_letters)

    if reverse_word == word:
        return True

    return False


if __name__ == "__main__":
    word = str(input('Write a word: '))

    palindrome_word_for(word)
