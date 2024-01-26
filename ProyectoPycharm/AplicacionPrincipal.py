# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AplicacionPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(371, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listDepartamento = QListWidget(self.centralwidget)
        self.listDepartamento.setObjectName(u"listDepartamento")

        self.gridLayout.addWidget(self.listDepartamento, 7, 0, 1, 1)

        self.LabelNombreDepartemento = QLabel(self.centralwidget)
        self.LabelNombreDepartemento.setObjectName(u"LabelNombreDepartemento")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelNombreDepartemento.sizePolicy().hasHeightForWidth())
        self.LabelNombreDepartemento.setSizePolicy(sizePolicy)
        self.LabelNombreDepartemento.setTextFormat(Qt.AutoText)
        self.LabelNombreDepartemento.setAlignment(Qt.AlignCenter)
        self.LabelNombreDepartemento.setMargin(10)

        self.gridLayout.addWidget(self.LabelNombreDepartemento, 0, 0, 1, 2)

        self.listaUsuario = QListWidget(self.centralwidget)
        self.listaUsuario.setObjectName(u"listaUsuario")

        self.gridLayout.addWidget(self.listaUsuario, 7, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.EditorNuevaNota = QTextEdit(self.centralwidget)
        self.EditorNuevaNota.setObjectName(u"EditorNuevaNota")

        self.verticalLayout_3.addWidget(self.EditorNuevaNota)

        self.BotonGuardarNota = QPushButton(self.centralwidget)
        self.BotonGuardarNota.setObjectName(u"BotonGuardarNota")

        self.verticalLayout_3.addWidget(self.BotonGuardarNota)


        self.gridLayout.addLayout(self.verticalLayout_3, 6, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BotonTopNotasLikeadas = QPushButton(self.centralwidget)
        self.BotonTopNotasLikeadas.setObjectName(u"BotonTopNotasLikeadas")
        self.BotonTopNotasLikeadas.setCheckable(False)

        self.verticalLayout.addWidget(self.BotonTopNotasLikeadas)

        self.BotonTopEmpleados = QPushButton(self.centralwidget)
        self.BotonTopEmpleados.setObjectName(u"BotonTopEmpleados")

        self.verticalLayout.addWidget(self.BotonTopEmpleados)

        self.BotonTopNotasComentadas = QPushButton(self.centralwidget)
        self.BotonTopNotasComentadas.setObjectName(u"BotonTopNotasComentadas")

        self.verticalLayout.addWidget(self.BotonTopNotasComentadas)


        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LabelNombreDepartemento.setText(QCoreApplication.translate("MainWindow", u"Nombre Del Departamento :", None))
        self.EditorNuevaNota.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nueva nota</p></body></html>", None))
        self.BotonGuardarNota.setText(QCoreApplication.translate("MainWindow", u"Guardar Nota", None))
        self.BotonTopNotasLikeadas.setText(QCoreApplication.translate("MainWindow", u"Top 3 notas Likeadas", None))
        self.BotonTopEmpleados.setText(QCoreApplication.translate("MainWindow", u"Top Empleados con mas Notas comentadas", None))
        self.BotonTopNotasComentadas.setText(QCoreApplication.translate("MainWindow", u"Top Notas con mas Comentarios", None))
    # retranslateUi

