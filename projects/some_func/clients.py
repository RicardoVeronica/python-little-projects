clients = [
            {'Name':'Ricardo', 'Appelido':'Duran', 'NSS':'100685A'},
            {'Name':'Victoria', 'Apellido':'Cortes', 'NSS':'291194'}
          ]


def show_client(clients_list, nss):
    for client in clients:
        if nss == clients['NSS']:
            print('Client: {} {}'.format(client['Name'], client['Apellido']))


print(show_client(clients, '291194'))
