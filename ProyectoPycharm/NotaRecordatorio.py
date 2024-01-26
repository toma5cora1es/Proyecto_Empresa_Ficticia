from Nota import Nota

class NotaRecordatorio(Nota):

    def __init__(self, DataBaseCursor, id):
        super().__init__(DataBaseCursor, id)


