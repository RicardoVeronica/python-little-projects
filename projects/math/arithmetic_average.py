"""
File: arithmetic_average.py
Author: setcain
Email: setcain@email.com
Github: https://github.com/setcain
Description: Arithmetic average with function
"""

my_list = [10, 9, 10, 8, 6]


def arithmetic_average(some_list):
    """ DOC of arithmetic_average

    some_list: Input of some list
    return: return the Arithmetic average

    """
    total = 0
    lenght = 0

    for i in my_list:
        total += i
        lenght += 1

    operation = total / lenght

    return operation


result = arithmetic_average(my_list)
print('The average of {} \nIs: {}'.format(my_list, result))
