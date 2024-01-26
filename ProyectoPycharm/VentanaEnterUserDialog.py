from PySide6.QtWidgets import QLabel, QLineEdit, QGridLayout, QDialogButtonBox, QDialog
from PySide6.QtGui import QIntValidator, Qt



class VentanaInicio(QDialog):
    def __init__(self, parent=None ):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.label = QLabel("Ingrese su id de usuario")
        self.labelError = QLabel("...")
        self.LineEdit = QLineEdit()

        self.LineEdit.setValidator(QIntValidator())
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
