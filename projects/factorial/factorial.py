"""
File: factorial.py
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: factorial of a number
"""


# Functions
def fact(number):
    if number == 0:
        return 1

    return number * fact(number - 1)


# Main method
if __name__ == "__main__":
    number = int(input('Write a number: '))
    res = fact(number)

    print(res)
