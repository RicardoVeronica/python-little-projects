"""
File: phonebook
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: simple phonebook in python
"""

# Main method
if __name__ == '__main__':

    # Init
    print('=== Welcome to the Phonebook ===')

    # Menu
    while True:
        user = str(input('''
            What do you want to do?..
            [a]dd a contact
            [r]emove a contact
            [s]ee a contact
            [l]ist all contact
            '''))