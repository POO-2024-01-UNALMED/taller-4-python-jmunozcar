from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo = "grupo predeterminado",  asignaturas = None, estudiantes = None):
        self._grupo = grupo
        if asignaturas is None:
            asignaturas = []
        self.asignaturas = asignaturas
        if estudiantes is None:
            estudiantes = []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, kwargs):
        for x in kwargs.values():
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno, lista = None):
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        myStr = "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre = "Grado 6"):
        cls.grado = nombre

