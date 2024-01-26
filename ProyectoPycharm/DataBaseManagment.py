from random import randint

class DataBaseManagment:
    def __init__(self, DataBaseCursor,id=None):
        self.cursor = DataBaseCursor
        self.id = id

    def genararClavePrimaria(self, tabla, id_tag):
        # genera problemas de concurrencia
        while True:
            test_id = randint(0, 100000)

            query = """select {id_tag:s} from {tabla:s} t
             where t.{id_tag:s} = {test_id:n}""".format(id_tag=id_tag, tabla=tabla, test_id=test_id)

            self.cursor.execute(query)

            if self.cursor.fetchone() is None:
                break

        return test_id

    def getListafromDataBase(self, query, constructor):

        self.cursor.execute(query)
        Lista = []

        while True:
            ControlElement = self.cursor.fetchone()
            if ControlElement is None:
                break
            else:
                auxId, = ControlElement
                Lista.append(constructor(self.cursor, auxId))

        return Lista

    def getId(self):
        return self.id

    def InsertEmpleado(self, nombre, id_departamento):

        add_data_query = ("INSERT INTO Empleados "
                          "( id_empleado , id_departamento, Nombre_empleado, edad) "
                          "VALUES (  %(id_empleado)s , %(id_departamento)s, %(Nombre_empleado)s, %(edad)s)")

        clave_generada = self.genararClavePrimaria('Empleados', 'id_empleado')

        # Insert Empleado information
        data = {
            'id_empleado': clave_generada,
            'id_departamento': id_departamento,
            'Nombre_empleado': nombre,
            'edad': randint(1, 40)
        }

        self.cursor.execute(add_data_query, data)

    def InsertNota(self, contenido, id_empleado):

        add_data_query = ("INSERT INTO Notas "
                          "( id_empleado, contenido) "
                          "VALUES ( %(id_empleado)s, %(contenido)s)")

        # Insert Nota information
        data = {
            'id_empleado': id_empleado,
            'contenido': contenido
        }

        self.cursor.execute(add_data_query, data)

        # Make sure data is committed to the database
        # self.connector.commit()

    def InsertLike(self, id_nota, id_empleado):

        # segmento de control

        query = """
        select * from Likes l
          where l.id_nota = {id_nota:n}
          and l.id_empleado = {id_empleado:n}
          """.format(id_empleado=id_empleado, id_nota=id_nota)

        self.cursor.execute(query)

        ControlVariable = self.cursor.fetchone()

        if ControlVariable is None:
            add_data_query = ("INSERT INTO Likes "
                              "( id_empleado, id_nota) "
                              "VALUES ( %(id_empleado)s , %(id_nota)s )")

            # Insert Like information
            data = {
                'id_empleado': id_empleado,
                "id_nota": id_nota
            }

            self.cursor.execute(add_data_query , data)
            return True
        else:
            return False

    def InsertComment(self, contenido, id_nota, id_empleado):

        # segmento de control
        #
        query = """
        select * from Comentarios c
          where c.id_nota = {id_nota:n} 
          and c.id_empleado = {id_empleado:n}
          """.format(id_empleado=id_empleado, id_nota=id_nota)

        self.cursor.execute(query)

        if self.cursor.fetchone() is not None:
            return False
        #
        #

        add_data_query = ("INSERT INTO Comentarios "
                          "( id_empleado, id_nota ,contenido) "
                          "VALUES ( %(id_empleado)s, %(id_nota)s, %(contenido)s )")

        # Insert Like information
        data = {
            'id_empleado': id_empleado,
            'id_nota': id_nota,
            'contenido':contenido
        }

        self.cursor.execute(add_data_query, data)

        return True

    def isEmpleadoinDatabase(self,id_empleado):

        if id_empleado == '':
            return False

        query = """select * from Empleados e
          where e.id_empleado = {id_empleado:s} 
          """.format(id_empleado=id_empleado)

        self.cursor.execute(query)

        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

