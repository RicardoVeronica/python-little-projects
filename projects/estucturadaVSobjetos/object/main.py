class Cliente:
    def __init__(self, id_cliente, nombre_cliete, apellidos_cliente):
        self.id_cliente = id_cliente
        self.nombre_cliete = nombre_cliete
        self.apellidos_cliente = apellidos_cliente

    def __str__(self):
        return '{} {}'.format(self.nombre_cliete, self.apellidos_cliente)


class Empresa:
    def __init__(self, lista_clientes=[]):
        self.lista_clientes = lista_clientes

    def mostrar_cliente(self, id_cliente='None'):
        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_cliente:
                print(cliente)

    def borrar_cliente(self, id_cliente='None'):
        for iterador, cliente in enumerate(self.lista_clientes):
            if cliente.id_cliente == id_cliente:
                del(self.lista_clientes[iterador])
                print(str(cliente), '> BORRADO')


# Instancias de clase Cliente
hector = Cliente(nombre_cliete='Hector', apellidos_cliente='Costa Guzman',
                 id_cliente='1A')

juan = Cliente(nombre_cliete='Juan', apellidos_cliente='Gonzales Marquez',
               id_cliente='2A')

# Instancia de clase Empresa
empresa = Empresa(lista_clientes=[hector, juan])
