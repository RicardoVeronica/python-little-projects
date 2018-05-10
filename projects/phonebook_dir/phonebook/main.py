"""
File: phonebook
Author: setcain
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: simple phonebook in python
"""

contacts = {}  # var - dict


def add_contact():
    name = input('\nGive a name for you new contact: ')
    name = name.upper()

    try:
        phone = int(input('Give a number for you new contact: '))
        contacts[name] = phone

        print('\nContact: {}\nPhone number: {}\nAdded'.format(name, phone))

    except ValueError:
        print('\nWrite a phone number')


def update_contact():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        contact_to_change = str(input('\nGive me the name to update: '))
        contact_to_change = contact_to_change.upper()

        change_number = int(input('Write the new number: '))
        contacts[contact_to_change] = change_number

        print('\nThe contact {} has change number for {}'.
          format(contact_to_change, change_number))


def remove_conntact():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        name = str(input('\nGive me the name of the contact to delete: '))
        name = name.upper()
        contacts.pop(name)

        print('\nThe contact {} was deleted'.format(name))


def see_a_contact():
    if len(contacts) == 0:
        print("\nYou don't have any contact")
    else:
        contact = str(input('\nGive me the name for the query: '))
        contact = contact.upper()

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
            print('\n{} - {} : {}'.format(idx + 1, contact,
                  contacts[contact]))


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
