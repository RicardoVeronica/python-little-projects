"""
File: simple-calculator
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: simple calculator whit python
"""


def add(one, two):
    return one + two


def sub(one, two):
    return one - two


def times(one, two):
    return one * two


def div(one, two):
    return one / two


def main():
    print('=== S I M P L E  C A L C U L A T O R ===')

    while True:
        print('''
            What do you want to do?:
            1 Addition
            2 Substraction
            3 Multiplication
            4 Divition
            5 Out
        ''')

        USER = int(input('What is youre choose? '))

        if USER == 1:
            NUM1 = float(input('Give me the first number:\t'))
            NUM2 = float(input('Give me the second number:\t'))

            sum_method = add(NUM1, NUM2)

            print(' \n===== Result: {}'.format(sum_method))

        elif USER == 2:
            NUM1 = float(input('Give the first number:\t'))
            NUM2 = float(input('Give the second number:\t'))

            sub_method = sub(NUM1, NUM2)

            print(' \n===== Result: {}'.format(sub_method))

        elif USER == 3:
            NUM1 = float(input('Give me the first number:\t'))
            NUM2 = float(input('Give me the second number:\t'))

            times_method = times(NUM1, NUM2)

            print(' \n===== Result: {}'.format(times_method))

        elif USER == 4:
            NUM1 = float(input('Give me the first number:\t'))
            NUM2 = float(input('Give me the second number:\t'))

            div_method = div(NUM1, NUM2)

            print(' \n===== Result: {}'.format(div_method))

        elif USER == 5:

            print('=== Bye ===')
            break

        else:

            print('=== Give me a valid option ===')


if __name__ == '__main__':
    main()
