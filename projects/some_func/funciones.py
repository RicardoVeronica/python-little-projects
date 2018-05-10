"""
File: funciones.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Funcioes ejemplos
"""


def some_tuple(*args):  # Returns tuple
    return args


print(some_tuple('pepe', 3, [1, 4.5]))


def some_dict(**kwargs):  # Returns dict
    return kwargs


print(some_dict(sexo=True, number=5, float_number=100.1))


def some_sum(a, b):
    return a + b


print(some_sum(10, 5))


def count(num):
    if num > 0:
        print(num)
        num -= 1
        count(num)


print(count(10))


def factorial(num):
    if num > 1:
        num = num * factorial(num - 1)

    return num


print(factorial(5))
