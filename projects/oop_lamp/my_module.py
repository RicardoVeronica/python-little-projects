class Lamp:
    _LAMPS = [
              '''
                  .
              .   |   .
               \     /
                  ()
                  --
                |____|
              ''', 
              '''
                  ()
                  __
                |____|
              '''
              ]

    # Construct
    def __init__(self):
        # Atributos
        self._on = False

    # Metodos
    def turn_on(self):
        self._on = True
        self._display_image()

    def turn_off(self):
        self._on = False
        self._display_image()

    def _display_image(self):
        if self._on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
