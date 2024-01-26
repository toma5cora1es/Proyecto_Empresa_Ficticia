from DataBaseManagment import DataBaseManagment

class Comentario(DataBaseManagment):

    def __init__(self, DataBaseCursor, id):

        super().__init__(DataBaseCursor, id)

    def getContenido(self):
        query = """select contenido from Comentarios c 
                where c.id_comentario = {id:n} """.format(id=self.id)
        self.cursor.execute(query)
        contenido, = self.cursor.fetchone()
        return contenido

    def getNombreEmpleado(self):
        query = """select Nombre_empleado from Comentarios c,Empleados e
                        where c.id_comentario  = {id:n}
                        and e.id_empleado = c.id_empleado""".format(id=self.id)
        self.cursor.execute(query)
        Nombre, = self.cursor.fetchone()
        return Nombre

    def getIdNota(self):
        query = """select id_nota from Comentarios c
                        where c.id_comentario  = {id:n}""".format(id=self.id)
        self.cursor.execute(query)
        id, = self.cursor.fetchone()
        return id