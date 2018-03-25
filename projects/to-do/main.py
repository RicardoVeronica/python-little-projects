"""
File: to-do/main.py
Author: setcain
Email: setcain@gmail.com
Github: https://github.com/setcain
Description: Todo list
"""

# Vars
var_list = []


# Functions
def show_list():
    """TODO: Docstring for show_list.
    :returns: Show the list whit or whitout items
    """
    if len(var_list) == 0:
        print("You don't have any item in your list")
    else:
        print('This is your list {}'.format(var_list))
        

def add_item():
    """TODO: Docstring for add_item.
    :returns: Add one item on the list
    """
    user = input('Give me item of the item to add on your list: ')
    var_list.append(user)
    print('Item {} has added to your list'.format(user))


def remove_item():
    """TODO: Docstring for remove_item.
    :returns: TODO
    """
    user = input('Give me the name of the item to remove: ')
    var_list.remove(user)
    print('Item {} has remove from your list'.format(user))


def main():
    """TODO: Docstring for main.
    :returns: App menu
    """
    # Init
    print('=== T O  D O  L I S T ===')

    while True:
        option = int(input('''
            What do you want to do?
            [1] See your list
            [2] Add item
            [3] Remove item
            [0] Out
        '''))

        # Call functions
        if option == 1:
            show_list()

        elif option == 2:
            add_item()

        elif option == 3:
            remove_item()

        elif option == 0:
            print('Ok, bye')
            break

        else:
            print('Give me a valid number')


# Main method
if __name__ == '__main__':
    main()
