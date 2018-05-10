from my_module import Lamp

def run():
    my_lamp = Lamp()

    while True:
        user = int(input('''
            Want do you want to do?
            [1] prender
            [2] apagar
            [3] salir
            '''))

        if user == 1:
            my_lamp.turn_on()
        elif user == 2:
            my_lamp.turn_off()
        else:
            break


if __name__ == "__main__":
    run() 
