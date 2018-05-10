class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película", self.titulo)

    # Destructor de clase
    def __del__(self):
        print("Se está borrando la película", self.titulo)

    # Redefinimos el método string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(
                self.titulo, self.lanzamiento, self.duracion)

    def __len__(self):
        return self.duracion


el_padrino = Pelicula("El Padrino", 175, 1972)
print(str(el_padrino))
print(len(el_padrino))
