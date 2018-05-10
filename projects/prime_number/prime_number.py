"""
File: prime_number.py
Author: setcain
Email: setcain00@email.com
Github: https://github.com/setcain
Description: know if a number is prime number
"""


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False

    return True


if __name__ == "__main__":
    number = int(input('Write a number: '))
    result = is_prime(number)

    if result is True:
        print('The number is prime')
    else:
        print('The number is not prime')
