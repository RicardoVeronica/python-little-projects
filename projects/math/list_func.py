"""
File: functions.py
Author: setcain
Email: setcain@mail.com
Github: https://github.com/setcain
Description: Some exercise
"""

my_data = [1, 22.5, 'my_name', 8.8, 4, 'my_age']


def average(arg1):
    """TODO: Docstring for average.

    arg1: some list or tuple
    :returns: two list or tuple whit strings or numbers content

    """
    # Function vars
    numbers = []
    strings = []

    for item in my_data:
        if isinstance(item, float) or isinstance(item, int):
            numbers.append(item)
        elif isinstance(item, str):
            strings.append(item)

    return numbers, strings


result = average(my_data)
print('''This is the result:
      Original list: {}
      Numbers: {}
      Strings: {}'''.format(my_data, result[0], result[1]))
