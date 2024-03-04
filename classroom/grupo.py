from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo = "grupo predeterminado",  asignaturas = None, estudiantes = None):
        self._grupo = grupo
        if asignaturas is None:
            asignaturas = []
        self._asignaturas = asignaturas
        if estudiantes is None:
            estudiantes = []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, kwargs):
        for x in kwargs.values():
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno, lista = []):
        lista.append(alumno)
        self.listadoAlumnos.append(lista)

    def __str__(self):
        myStr = "Grupo de estudiantes: " + self._grupo
        return myStr

    @ classmethod
    def asignarNombre(cls, nombre = "Grado 6"):
        cls.grado = nombre
