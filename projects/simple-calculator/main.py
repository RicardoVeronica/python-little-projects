'''Simple calculator whit options'''


def add(one, two):
    return one + two


def sub(one, two):
    return one - two


def mul(one, two):
    return one * two


def div(one, two):
    return one / two


if __name__ == '__main__':

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

        USER = input('What is youre choose? ')

        if USER == '1':

            NUM1 = float(input('Give me the first number:\t'))

            NUM2= float(input('Give me the second number:\t'))

            print('=== Result:', add(NUM1, NUM2))

        elif USER == '2':

            NUM1 = float(input('Give the first number:\t'))

            NUM2 = float(input('Give the second number:\t'))

            print('=== Result:' ,sub(NUM1, NUM2))

        elif USER == '3':

            NUM1 = float(input('Give me the first number:\t'))

            NUM2 = float(input('Give me the second number:\t'))

            print('=== Result:', mul(NUM1, NUM2))

        elif USER == '4':

            NUM1 = float(input('Give me the first number:\t'))

            NUM2 = float(input('Give me the second number:\t'))

            print('=== Result:', div(NUM1, NUM2))

        elif USER == '5':

            print('=== Bye ===')

            break

        else:

            print('=== Give me a valid option ===')

