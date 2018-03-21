articles = []


def add_item():
    item = input('\nGive me the name of the item to add: ')
    item = item.capitalize()
    articles.append(item)

    print('\n===== Item {} added to your list =====\n'.format(item))


def delete_item():
    item = input('\nGive me the name of item to delete: ')
    item = item.capitalize()
    articles.remove(item)

    print('\n===== The item {} has been deleted =====\n'.format(item))


def see_list():
    if len(articles) < 1:
        print('\n=== Your list is empty, add some items ===\n')
    else:
        print('\n===== This is your list =====\n')
        for item in articles:
            print('{}\n'.format(item))


def main():
    while True:
        print('====== S H O P  L I S T ======')
        print('''
              Welcom to -SHOP LIST- What do yo want to do?\n
              [1] Add item to your list
              [2] Delete item from your list
              [3] See your list
              [4] Out
              ''')
        user = int(input('What is your choice: '))

        if user < 1 or user > 4:
            print('\n ===== Give me a valid option =====\n')
        elif user == 1:
            add_item()
        elif user == 2:
            delete_item()
        elif user == 3:
            see_list()
        elif user == 4:
            print('\nThank you for using === SHOP LIST === See you later')
            break


if __name__ == "__main__":
    main()
