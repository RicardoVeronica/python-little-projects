""" A simple shop list for practice python language
Shop list:
    Add item
    Remove item
    Show items
"""

# Vars
shop_list = list()


# Functions
def add_item():
    """
    Add an item in the var list
    """
    print('Add an item')
    item = input('Item name: ')
    shop_list.append(item)


def remove_item():
    """
    Delete an item from the var list
    """
    print('remove some item') 


def see_list():
    """
    See the var list items
    """
    print('see your list') 


def no_option():
    """
    If the user put any unavailable option show this message
    """
    print('No available option, try again')


# Main
if __name__ == '__main__':

    # Vars
    valid_options = [0, 1, 2, 3]
    
    # Init
    print('===== S H O P  L I S T =====')

    # Option menu
    while True:
        user = int(input('''
            Wellcome what do you want to do?
            [1] Add item to your list
            [2] Remove item to your list
            [3] See your list
            [0] Out from app
            '''))

        if user == valid_options[1]:
            add_item()
        elif user == valid_options[2]:
            remove_item()
        elif user == valid_options[3]:
            see_list()
        elif user == valid_options[0]:
            print('See you later...')
            break
        elif user not in valid_options:
            no_option()

else:
    print('Something is broken')

