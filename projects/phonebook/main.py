"""
File: phonebook
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: simple phonebook in python
"""

contacts = {}


def add_contact():
    name = input('\nGive a name for you new contact: ')
    name = name.capitalize()

    try:
        phone = int(input('Give a number for you new contact: '))
        contacts[name] = phone

        print('\ncontact {}, added. phone number {}'.format(name, phone))

    except ValueError:
        print('\nWrite a phone number')


def update_contact():
    if len(contacts) == 0:
        print("\nYou dont't have any contact")
    else:
        contact_to_change = input('\nGive me the name to update: ')
        contact_to_change = contact_to_change.capitalize()

        change_number = input('Write the new number: ')
        contacts[contact_to_change] = change_number

        print('\nThe contact {} has change number for {}'.
              format(contact_to_change, change_number))


def remove_conntact():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        name = input('\nGive me the name of the contact to delete: ')
        name = name.capitalize()
        contacts.pop(name)

        print('\nThe contact {} was deleted'.format(name))


def see_a_contact():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        contact = input('\nGive me the name for the query: ')
        contact = contact.capitalize()

        if contact in contacts:
            query = contacts[contact]

            print('\n{} : {}'.format(contact, query))
        else:
            print('\nContact {}, do not exist'.format(contact))


def see_all_contacts():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        for idx, contact in enumerate(contacts):
            print('\n{} - {} : {}'.format(idx + 1, contact, contacts[contact]))


def clear_phonebook():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        contacts.clear()

        print('\nThe phonebook is clear')


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
            msg = '\nWrite just integers numbers for this option...'
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
