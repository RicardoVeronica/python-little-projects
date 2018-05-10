"""
File: phonebook
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/SetCain/python-basics/tree/master/projects/
        phonebook-obj
Description: simple phonebook in python
"""

from module import Phonebook

# Main method
if __name__ == '__main__':

    instance = Phonebook()

    # Init
    print('=== Welcome to the Phonebook ===')

    # Menu
    while True:
        MENU = print('''
            What do you want to do?
            [1] Add a contact
            [2] Update contact
            [3] Remove a contact
            [4] See a contact
            [5] List all contact
            [6] Clear the phonebook
            [0] Out
            ''')
        try:
            MSG = '\nWrite a valid option...'
            user = int(input('What do you want to do? '))

            if user == 1:
                instance.add_contact()
            elif user == 2:
                instance.update_contact()
            elif user == 3:
                instance.remove_conntact()
            elif user == 4:
                instance.see_a_contact()
            elif user == 5:
                instance.see_all_contacts()
            elif user == 6:
                instance.clear_phonebook()
            elif user == 0:
                print('Ok goodby')
                break
            else:
                print(MSG)

        except ValueError:
            print(MSG)
