class Phonebook:

    # Constructor
    def __init__(self):
        self._contacts = {}

    def add_contact(self):
        name = input('\nGive a name for you new contact: ')
        name = name.upper()

        try:
            phone = int(input('Give a number for you new contact: '))
            self._contacts[name] = phone

            print('\nContact: {}\nPhone number: {}\nAdded'.format(name,
                                                                  phone))

        except ValueError:
            print('\nWrite a phone number')

    def update_contact(self):
        if len(self._contacts) == 0:
            print("\nYou dont't have any contact")
        else:
            contact_to_change = input('\nGive me the name to update: ')
            contact_to_change = contact_to_change.upper()

            change_number = input('Write the new number: ')
            self._contacts[contact_to_change] = change_number

            print('\nThe contact {} has change number for {}'.
                  format(contact_to_change, change_number))

    def remove_conntact(self):
        if len(self._contacts) == 0:
            print("\nYou don't have any contact")
        else:
            name = input('\nGive me the name of the contact to delete: ')
            name = name.upper()
            self._contacts.pop(name)

            print('\nThe contact {} was deleted'.format(name))

    def see_a_contact(self):
        if len(self._contacts) == 0:
            print("\nYou don't have any contact")
        else:
            contact = input('\nGive me the name for the query: ')
            contact = contact.upper()

            if contact in self._contacts:
                query = self._contacts[contact]

                print('\nNAME: {}\nNumber: {}'.format(contact, query))
            else:
                print('\nContact {}, do not exist'.format(contact))

    def see_all_contacts(self):
        if len(self._contacts) == 0:
            print("\nYou don't have any contact")
        else:
            for idx, contact in enumerate(self._contacts):
                print('\n{} - \nNAME: {}\nNUMBER: {}'.format(idx + 1, contact,
                      self._contacts[contact]))

    def clear_phonebook(self):
        if len(self._contacts) == 0:
            print("\nYou don't have any contact")
        else:
            self._contacts.clear()

            print('\nThe phonebook is clear')
