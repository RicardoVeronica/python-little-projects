"""
File: ex.py
Author: setcain
Email: setcain@mail.com
Github: https://github.com/setcain
Description: Arithmetic average
"""
items = ['abc', '1, 2, 3', 9, 9, 7, 6, 8.5, 7, 9.5, 'hello', 10, 6, 'world']


def parse_list(some_list):
    num_list = []
    str_list = []

    for item in items:
        if isinstance(item, float) or isinstance(item, int):
            num_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)

    return num_list, str_list


def count_num_items(some_list):
    total = 0

    for item in items:
        if isinstance(item, int) or isinstance(item, float):
            total += item

    return total


def avg():
    arithmetic_avg = count_num_items(items) / len(items)

    return 'Arithmetic average: {:.2f}'.format(arithmetic_avg)


print(avg())
print(count_num_items(items))
print(parse_list(items))


def separate_and_count(some_list):
    pass
