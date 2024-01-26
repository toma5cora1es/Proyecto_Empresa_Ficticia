from DataBaseManagment import DataBaseManagment

class Like(DataBaseManagment):

    def __init__(self, DataBaseCursor, id):

        super().__init__(DataBaseCursor, id)

        query = """select id_empleado, id_nota from Likes l  
        where l.id_like = {id:n}""".format(id=self.id)

        self.cursor.execute(query)

        self.id_empleado, self.id_nota = self.cursor.fetchone()

