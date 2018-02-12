''' To do list '''

# Vars
var_list = list()


# Functions
def show_list():
    if len(var_list) == 0:
        print('There are no items on your list')
    else:
        print('---------- This is your list: ----------\n')
        for element in var_list:
            print(element)


def add_item():
    name = input('What is the name of the new item... ')

    add_content = input('Do you want to put extra info on the item? [y/n]: ')
    if add_content == 'y':
        content = input('Write content here... ')
    elif add_content == 'n':
        content = ' '
    else:
        print('Press "y" for yes or "n" for no, try again')
        return add_item()

    item = {'name_key': name, 'content_key': content}

    var_list.append(item)
    print('''
            Item added on your list:
            Name "{}" 
            Content "{}" '''.format(name.capitalize(), content.capitalize()))


def remove_item():
    clean = input('Whats the name of the item... ')
    del(var_list[clean])


def update_item():
    pass



def delete_list():
    pass


def say_good_bye():
    print('ok good bye') 


def what_the():
    print('Option invalid, try again')


# Main method
if __name__ == '__main__':

    # Init
    print('=== T O  D O  L I S T ===')

    # Menu
    while True:
        user = int(input('''
                What do you want to do?
                [1] See your list
                [2] Add item
                [3] Remove item
                [4] Update item
                [5] Delete all list
                [6] Out
                '''))
        
        # Call functions
        if user == 1:
            show_list()
        elif user == 2:
            add_item()
        elif user == 3:
            remove_item()
        elif user == 4:
            update_item()
        elif user == 5:
            delete_list()
        elif user == 6:
            say_good_bye()
            break
        else:
            what_the()
