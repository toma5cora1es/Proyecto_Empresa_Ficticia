from Nota import Nota
from Like import Like
from Comentario import Comentario
import random

from DataBaseManagment import DataBaseManagment

class Empleado(DataBaseManagment):

    def __init__(self, DataBaseCursor, id):
        super().__init__(DataBaseCursor, id)

    def NuevaNota(self,contenido):
        self.InsertNota(contenido, self.id )

    def getNombre(self):
        query = """select Nombre_empleado from Empleados e, Departamentos d 
        where e.id_empleado = {id:n} and e.id_departamento = d.id_departamento""".format(id=self.id)
        self.cursor.execute(query)
        nombre, = self.cursor.fetchone()
        return nombre

    def getNombreDepartamento(self):
        query = """select Nombre_departamento from Empleados e, Departamentos d 
                where e.id_empleado = {id:n} and e.id_departamento = d.id_departamento""".format(id=self.id)
        self.cursor.execute(query)

        NombreDepartamento, = self.cursor.fetchone()
        return NombreDepartamento

    def getId_Departamento(self):
        query = """select id_departamento from Empleados e 
        where e.id_empleado = {id:n} """.format(id=self.id)

        self.cursor.execute(query)

        nombre, = self.cursor.fetchone()
        return nombre


    # def getListaNotas(self):
    #     query = """select id_nota from Empleados e, Notas n
    #                 where e.id_empleado = {id:n}
    #                 and n.id_empleado = e.id_empleado""".format(id=self.id)
    #
    #     lista = self.getListafromDataBase(query=query, constructor=Nota)
    #
    #     return lista

    def getListaLikes(self):
        query = """select id_like from Notas n,Likes l,Empleados e
                    where e.id_empleado = {id:n} and 
                          e.id_empleado = n.id_empleado and 
                          n.id_nota = l.id_nota """.format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Like)

        return lista

    def getListaComentarios(self):
        query = """select id_Comentario from Notas n,Comentarios c,Empleados e
                    where e.id_empleado = {id:n} and 
                          e.id_empleado = n.id_empleado and 
                          n.id_nota = c.id_nota""".format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Comentario)

        return lista

    def getListaNotas(self):
        query = """select id_nota from Notas n ,Empleados e
                    where e.id_empleado = {id:n} and 
                          e.id_empleado = n.id_empleado""".format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Nota)

        return lista