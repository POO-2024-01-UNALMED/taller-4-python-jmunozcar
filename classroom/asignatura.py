class Asignatura:

    def __init__(self, nombre, salon = "503B"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        myString = self._nombre + " " + self._salon
