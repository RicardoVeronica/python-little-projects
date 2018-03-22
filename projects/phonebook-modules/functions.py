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
