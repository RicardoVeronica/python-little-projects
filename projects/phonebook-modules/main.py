"""
File: phonebook
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/SetCain/python-basics/tree/master/projects/
        phonebook-modules 
Description: simple phonebook in python
"""
from functions import add_contact, update_contact, remove_conntact,\
    see_a_contact, see_all_contacts, clear_phonebook

# Main method
if __name__ == '__main__':

    # Init
    print('=== Welcome to the Phonebook ===')

    # Menu
    while True:
        user = print('''
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
            msg = '\nWrite a valid option...'
            user = int(input('What do you want to do? '))

            if user == 1:
                add_contact()
            elif user == 2:
                update_contact()
            elif user == 3:
                remove_conntact()
            elif user == 4:
                see_a_contact()
            elif user == 5:
                see_all_contacts()
            elif user == 6:
                clear_phonebook()
            elif user == 0:
                print('Ok goodby')
                break
            else:
                print(msg)

        except ValueError:
            print(msg)
