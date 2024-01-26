from Empleado import Empleado
from DataBaseManagment import DataBaseManagment

class Departamento(DataBaseManagment):
    def __init__(self, DataBaseCursor, id):
        super().__init__(DataBaseCursor, id)

    def getNombre(self):
        query = """select Nombre_departamento from Departamentos d 
               where d.id_departamento = {id:n} """.format(id=self.id)

        self.cursor.execute(query)

        nombre, = self.cursor.fetchone()

        return nombre

    def getListaEmpleados(self):
        query = """select id_empleado from Empleados e, Departamentos d 
                    where e.id_departamento = {id:n} 
                    and d.id_departamento = e.id_departamento""".format(id=self.id)

        lista = self.getListafromDataBase(query=query, constructor=Empleado)

        return lista