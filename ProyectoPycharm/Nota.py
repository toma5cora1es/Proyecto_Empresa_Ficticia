from Like import Like
from Comentario import Comentario
from DataBaseManagment import DataBaseManagment


class Nota(DataBaseManagment):

    def __init__(self, DataBaseCursor, id):

        super().__init__(DataBaseCursor, id)

    def NuevoComentario(self,contenido,id_empleado):
        self.InsertComment(contenido,self.id,id_empleado)

    def NuevoLike(self,id_usuario):
        return self.InsertLike(self.getId() , id_usuario)

    def getIdEmpleado(self):
        query = """select id_empleado from Notas n
                        where n.id_nota = {id:n}""".format(id=self.id)

        self.cursor.execute(query)

        contenido, = self.cursor.fetchone()

        return contenido

    def getContenido(self):
        query = """select contenido from Notas n
                        where n.id_nota = {id:n}""".format(id=self.id)

        self.cursor.execute(query)

        contenido, = self.cursor.fetchone()

        return contenido

    def getLikeNumber(self):
        query = """select count( id_nota ) 
                    from Likes where id_nota = {id:n}""".format(id=self.id)

        self.cursor.execute(query)

        control = self.cursor.fetchone()

        if control is None:
            NumeroLikes = 0
        else:
            NumeroLikes, = control

        return NumeroLikes


    def getNombreEmpleado(self):
        query = """select Nombre_empleado from Notas n,Empleados e
                        where n.id_nota = {id:n}
                        and e.id_empleado = n.id_empleado""".format(id=self.id)

        self.cursor.execute(query)

        nombre, = self.cursor.fetchone()

        return nombre

    def getListaLikes(self):
        query = """select id_like from Notas n,Likes l,Empleados e
                    where n.id_nota = {id:n} and 
                          e.id_empleado = n.id_empleado 
                          and n.id_nota = l.id_nota """.format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Like)

        return lista

    def isLikedBy(self,id_empleado):
        query = """select id_like from Notas n,Likes l,Empleados e
                    where n.id_nota = {id:n} and 
                          e.id_empleado = {id_empleado:n}
                          and n.id_nota = l.id_nota """.format(id=self.id,id_empleado=id_empleado)

        self.cursor.execute(query)

        ControlElement = self.cursor.fetchone()

        if ControlElement is None:
            return False
        else:
            return True


    def getListaComentarios(self):
        query = """select id_Comentario from Notas n,Comentarios c,Empleados e
                    where n.id_nota = {id:n} 
                    and e.id_empleado = n.id_empleado 
                    and n.id_nota = c.id_nota """.format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Comentario)

        return lista

