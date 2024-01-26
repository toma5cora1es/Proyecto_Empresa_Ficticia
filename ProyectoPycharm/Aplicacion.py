import sys
import mysql.connector
from Nota import Nota
from Empleado import Empleado
from Departamento import Departamento
from WidgetsDataBase import WidgetNota, WidgetEmpleado
from DataBaseManagment import DataBaseManagment

from VentanaEnterUserDialog import VentanaInicio
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,\
    QListWidgetItem, QListWidget
from AplicacionPrincipal import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # damos el formato a la aplicacion
        self.setupUi(self)

        # instanciar el conector a la base de datos
        self.connector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3141592",
            database="dbempresa"
        )

        self.connector.autocommit = True

        self.cursor = self.connector.cursor(buffered=True)

        self.IngresarUsuario()

        # conectamos los botones con sus funciones
        self.BotonTopNotasLikeadas.pressed.connect(self.print3NotasMasLikeadas)

        self.BotonGuardarNota.pressed.connect(self.GuardarNota)

        # mostramos la aplicacion
        self.show()

    def IngresarUsuario(self):

        self.DBManager = DataBaseManagment(DataBaseCursor=self.cursor)

        # mostrar una pantalla para elegir empleado
        while True:
            VentanaIngresarUsuario = VentanaInicio(self)
            VentanaIngresarUsuario.exec()
            id_usuario = VentanaIngresarUsuario.LineEdit.text()
            if self.DBManager.isEmpleadoinDatabase(id_usuario):
                break
        id_usuario = int(id_usuario)

        self.usuario = Empleado(self.cursor, id_usuario)

        self.departamento = Departamento(self.cursor, self.usuario.getId_Departamento())

        self.LabelNombreDepartemento.setText(self.usuario.getNombre()
                                             + ", Departamento de "
                                             + self.usuario.getNombreDepartamento()
                                             )
        self.printListaEmpleados()

        self.printListaNotas()

    def print3NotasMasLikeadas(self):
        self.ListaEmergente = QListWidget()
        label = QLabel("Lista de Notas del Departamento")
        item = QListWidgetItem()
        self.ListaEmergente.insertItem(self.listaUsuario.count(), item)
        self.ListaEmergente.setItemWidget(item, label)
        item.setSizeHint(label.sizeHint())
        query = """select n.id_nota 
        from likes l ,empleados e ,notas n 
        where 
        n.id_nota  = l.id_nota and
        l.id_empleado  = e.id_empleado  
        group by l.id_nota  
        order by count(l.id_nota) desc limit 3;"""

        ListaNotas = self.usuario.getListafromDataBase(query,Nota)

        for element in ListaNotas:
            WNota = WidgetNota(element, self.usuario.getId())
            item = QListWidgetItem()
            self.ListaEmergente.insertItem(self.ListaEmergente.count(), item)
            self.ListaEmergente.setItemWidget(item, WNota)
            item.setSizeHint(WNota.sizeHint())

        self.ListaEmergente.show()

    def printListaNotas(self):
        # modificar si se modifica la ui

        self.listaUsuario.clear()

        label = QLabel("Lista de Notas del Departamento")

        item = QListWidgetItem()
        self.listaUsuario.insertItem(self.listaUsuario.count(), item)
        self.listaUsuario.setItemWidget(item, label)
        item.setSizeHint(label.sizeHint())

        ListaNotas = self.usuario.getListaNotas()

        for element in ListaNotas:
            WNota = WidgetNota(element, self.usuario.getId())
            item = QListWidgetItem()
            self.listaUsuario.insertItem(self.listaUsuario.count(), item)
            self.listaUsuario.setItemWidget(item, WNota)
            item.setSizeHint(WNota.sizeHint())

    def printListaEmpleados(self):
        # modificar si se
        # modifica la ui

        self.listDepartamento.clear()

        label = QLabel("Lista de Empleados del Departamento")
        item = QListWidgetItem()
        self.listaUsuario.insertItem(self.listaUsuario.count(), item)
        self.listaUsuario.setItemWidget(item, label)
        item.setSizeHint(label.sizeHint())

        ListaEmpleados = self.departamento.getListaEmpleados()

        for element in ListaEmpleados:
            WEmpleado = WidgetEmpleado(element)
            item = QListWidgetItem()
            self.listDepartamento.insertItem(self.listaUsuario.count(), item)
            self.listDepartamento.setItemWidget(item, WEmpleado)
            item.setSizeHint(WEmpleado.sizeHint())

    def GuardarNota(self):
        self.usuario.NuevaNota(self.EditorNuevaNota.toPlainText())

        self.EditorNuevaNota.setText("")

        self.printListaNotas()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
