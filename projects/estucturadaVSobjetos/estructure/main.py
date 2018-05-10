'''
Simple example
'''

clients_list = []


def add_client(clients_list, client_id):
    pass


def show_client(client_id):
    for client in clients_list:
        if client_id == client['id']:
            print('Name: {} id: {}'.format(client['Name'],
                                           client['id']))


def delete_client(client_id):
    for iterator, client in enumerate(clients_list):
        if client_id == client['id']:
            del(clients_list[iterator])
            print('CLIENT DELETED > {}'.format(client['Name']))


if __name__ == '__main__':
    print('=== Welcome to my app ===')

    while True:
        user = print('''
                     What do you want to do?
                     [1] Add client
                     [2] Show client
                     [3] Delete client
                     [0] Out
                     ''')
        try:
            msg = '\n Write just integer numbers for this option'
            user = int(input('What is your choose'))

            if user == 1:
                add_client(client_name, client_id)
            elif user == 2:
                show_client(client_id)
            elif user == 3:
                delete_client(client_id)
            elif user == 0:
                print('Ok Goodbye')
                break
            else:
                print(msg)

        except ValueError:
            print(msg)
