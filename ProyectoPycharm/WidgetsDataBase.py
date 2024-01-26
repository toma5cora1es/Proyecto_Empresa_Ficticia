from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout, \
    QVBoxLayout, QLabel, QDialog, QGridLayout, QDialogButtonBox ,QTextEdit
from PySide6.QtGui import Qt, QPalette, QColor, QIcon



class WidgetNota(QWidget):

    def __init__(self, nota,Id_Usuario):
        super().__init__()

        self.DataBaseNota = nota
        self.UsuarioAplicacion = Id_Usuario
        self.SetupUi()

    def SetupUi(self):
        self.Hlayout = QHBoxLayout(self)
        # adding label
        self.label = QLabel( self.DataBaseNota.getContenido() )
        self.label.setWordWrap(True)
        self.label.setAutoFillBackground(True)


        # buttons
        self.LikeButton = QToolButton()
        self.ComentButton = QToolButton()
        self.LikeNumberButton =QToolButton()

        # adding icons
        self.LikeIcon = QIcon("tick.png")
        self.ComentIcon = QIcon("balloon.png")

        # setting icons
        self.LikeButton.setIcon(self.LikeIcon)
        self.ComentButton.setIcon(self.ComentIcon)


        # setting text
        self.LikeNumberButton.setText(str(self.DataBaseNota.getLikeNumber()))

        # connecting functions
        self.LikeButton.clicked.connect(self.LikeNote)
        self.ComentButton.clicked.connect(self.CommentNote)

        # adding buttons and label to layout
        self.Hlayout.addWidget(self.label)
        self.Hlayout.addWidget(self.LikeButton)
        self.Hlayout.addWidget(self.LikeNumberButton)
        self.Hlayout.addWidget(self.ComentButton)


    def CommentNote(self):
        self.DialogComentar = WidgetComentarNota(self, self.DataBaseNota)

        self.DialogComentar.exec()

        self.DataBaseNota.NuevoComentario(
            self.DialogComentar.LineEdit.toPlainText(),
            self.UsuarioAplicacion
        )

    def LikeNote(self):
        self.DataBaseNota.NuevoLike(self.UsuarioAplicacion)
        # setting text
        self.LikeNumberButton.setText(str(self.DataBaseNota.getLikeNumber()))

class WidgetComentarNota(QDialog):

    def __init__(self, parent=None, nota=None):
        # self.setupUi(self)
        super().__init__(parent)

        self.nota = nota

        self.setupUI()

    def setupUI(self):
        self.label = QLabel( str(self.nota.getId()) )
        self.labelError = QLabel("...")
        self.LineEdit = QTextEdit(self)

        self.LineEdit.selectAll()
        self.LineEdit.setAlignment(Qt.AlignCenter)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.labelError, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)


class WidgetEmpleado(QWidget):

    def __init__(self, empleado):
        super().__init__()

        self.DataBaseEmpleado = empleado
        self.SetupUi()

    def SetupUi(self):
        self.label = QLabel(self.DataBaseEmpleado.getNombre()
                            +
                            " del departamento de "
                            +
                            self.DataBaseEmpleado.getNombreDepartamento()
                            )
        self.label.setWordWrap(True)
        self.label.setAutoFillBackground(True)
        self.Hlayout = QHBoxLayout(self)
        self.Hlayout.addWidget(self.label)
        # buttons
        self.GearButton = QToolButton()
        self.NoteButton = QToolButton()
        # creating icons
        self.GearIcon = QIcon("balloon.png")
        self.NoteIcon = QIcon("sticky-notes-stack.png")
        # setting icons
        self.GearButton.setIcon(self.GearIcon)
        self.NoteButton.setIcon(self.NoteIcon)
        # connecting functions
        self.GearButton.clicked.connect(self.SeeComments)
        self.NoteButton.clicked.connect(self.SeeNotes)
        # adding buttons to layout
        self.Hlayout.addWidget(self.GearButton)
        self.Hlayout.addWidget(self.NoteButton)

        # self.Hlayout.addWidget(self.ComentButton)

    def SeeComments(self):
        self.widgetEmergente = QWidget()
        ListaComentariosEmpleado = self.DataBaseEmpleado.getListaComentarios()
        LayoutWidget = QVBoxLayout(self.widgetEmergente)
        LayoutWidget.addWidget( QLabel("Lista de Comentarios hechos por "
                                      + self.DataBaseEmpleado.getNombre() ) )

        for element in ListaComentariosEmpleado:
            LayoutWidget.addWidget(WidgetComentario(element))
        self.widgetEmergente.setLayout(LayoutWidget)
        self.widgetEmergente.show()

    def SeeNotes(self):
        self.widgetEmergente = QWidget()
        ListaNotasEmpleado = self.DataBaseEmpleado.getListaNotas()
        LayoutWidget = QVBoxLayout(self.widgetEmergente)
        LayoutWidget.addWidget(QLabel("Lista de Notas de "
                                      + self.DataBaseEmpleado.getNombre()))

        for element in ListaNotasEmpleado:
            LayoutWidget.addWidget(WidgetNota(element,self.DataBaseEmpleado.getId()))
        self.widgetEmergente.setLayout(LayoutWidget)
        self.widgetEmergente.show()

class WidgetComentario(QWidget):

    def __init__(self, comentario):
        super().__init__()

        self.DatabaseComentario = comentario
        self.contenido = QLabel("comentario : " + self.DatabaseComentario.getContenido())
        self.contenido.setWordWrap(True)

        self.contenido.setAutoFillBackground(True)
        palette = self.contenido.palette()
        palette.setColor(QPalette.Window, QColor("yellow"))
        self.contenido.setPalette(palette)

        self.NombreEmpleado = QLabel("Comentario del empleado  : \n" + self.DatabaseComentario.getNombreEmpleado())

        Vlayout = QHBoxLayout(self)

        Vlayout.addWidget(self.contenido)
        Vlayout.addWidget(self.NombreEmpleado)

        self.setLayout(Vlayout)

