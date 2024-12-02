from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class VentanaOpciones(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaOpciones, self).__init__()
        self.ui = Ui_Window_opciones()
        self.ui.setupUi(self)

        # Configurar ventana sin bordes
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.conectar_botones()

        # Habilitar los botones
        self.ui.pushButton_RegistarNuevoServicio.setEnabled(True)
        self.ui.pushButton_VerlistaDeservivios.setEnabled(True)
        self.ui.pushButton_Salir.setEnabled(True)

    def conectar_botones(self):
        self.ui.pushButton_RegistarNuevoServicio.clicked.connect(self.mostrar_registro_servicio)
        self.ui.pushButton_VerlistaDeservivios.clicked.connect(self.mostrar_lista_servicios)
        self.ui.pushButton_Salir.clicked.connect(self.cerrar_sesion)

    def mostrar_registro_servicio(self):
        from Ventana_RegistrarServicio import VentanaRegistrarServicio
        self.ventana_registro = VentanaRegistrarServicio()
        self.ventana_registro.show()
        self.hide()  # Cambiado de close() a hide()

    def mostrar_lista_servicios(self):
        from VentanaListaDeservicios import VentanaListaDeservicios
        self.ventana_lista = VentanaListaDeservicios()
        self.ventana_lista.show()
        self.hide()  # Cambiado de close() a hide()

    def cerrar_sesion(self):
        self.close()  # Esto cerrará la ventana actual
        # Buscar la ventana de login y mostrarla
        for widget in QtWidgets.QApplication.topLevelWidgets():
            if isinstance(widget, QtWidgets.QMainWindow) and widget.__class__.__name__ == 'VentanaLogin':
                widget.show()
                break


    def mostrar_lista_servicios(self):
        from VentanaListaDeservicios import VentanaListaDeservicios
        self.ventana_lista = VentanaListaDeservicios()
        self.ventana_lista.show()
        self.close()

    def cerrar_sesion(self):
        from VentanaLogin import VentanaLogin
        self.ventana_login = VentanaLogin()
        self.ventana_login.show()
        self.close()



class Ui_Window_opciones(object):
    def setupUi(self, Window_opciones):
        Window_opciones.setObjectName("Window_opciones")
        Window_opciones.resize(572, 520)
        self.centralwidget = QtWidgets.QWidget(Window_opciones)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 541, 491))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(250, 0, 291, 491))
        self.label.setStyleSheet("\n"
            "border-image: url(:/imagenes/japonanime-ciudad-pastel-fjnhzk0ixe2x3cub.webp);\n"
            "border-top-right-radius: 50px;\n"
            "\n"
            "                     border-bottom-right-radius: 50px;\n"
            "                     border: 1px solid #ccc;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 271, 491))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 1);\n"
            "               border-bottom-left-radius: 50px;\n"
            "border-top-left-radius: 50px;\n"
            "                     border: 1px solid #ccc;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 541, 141))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(38)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,75);\n"
            "\n"
            "border-top-left-radius: 50px;\n"
            "border-top-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton_RegistarNuevoServicio = QtWidgets.QPushButton(self.widget)
        self.pushButton_RegistarNuevoServicio.setEnabled(False)
        self.pushButton_RegistarNuevoServicio.setGeometry(QtCore.QRect(90, 180, 160, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_RegistarNuevoServicio.setFont(font)
        self.pushButton_RegistarNuevoServicio.setStyleSheet("    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,   \n"
            "                                       stop: 0 rgba(186, 85, 211, 255), /* Violeta claro */\n"
            "                                       stop: 1 rgba(138, 43, 226, 255)); /* Violeta oscuro */\n"
            "    color: rgba(255, 255, 255, 240); /* Texto blanco */\n"
            "    border: none;  \n"
            "    padding: 12px 20px;  \n"
            "    border-radius: 5px;  \n"
            "\n"
            "\n"
            "    cursor: pointer;\n"
            "    transition: background-color 0.3s ease, transform 0.2s ease;")
        self.pushButton_RegistarNuevoServicio.setObjectName("pushButton_RegistarNuevoServicio")
        self.pushButton_VerlistaDeservivios = QtWidgets.QPushButton(self.widget)
        self.pushButton_VerlistaDeservivios.setEnabled(False)
        self.pushButton_VerlistaDeservivios.setGeometry(QtCore.QRect(90, 270, 160, 61))
        self.pushButton_VerlistaDeservivios.setStyleSheet(" background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,   \n"
            "                                       stop: 0 rgba(138, 43, 226, 255), /* Violeta */\n"
            "                                       stop: 1 rgba(186, 85, 211, 255)); /* Violeta más claro */\n"
            "    color: rgba(255, 255, 255, 240); /* Texto blanco */\n"
            "    border: none;  \n"
            "    padding: 12px 20px;  \n"
            "    border-radius: 5px;  \n"
            "  \n"
            "    cursor: pointer;\n"
            "    transition: background-color 0.3s ease, transform 0.2s ease; /* Transiciones suaves */")
        self.pushButton_VerlistaDeservivios.setObjectName("pushButton_VerlistaDeservivios")
        self.pushButton_Salir = QtWidgets.QPushButton(self.widget)
        self.pushButton_Salir.setEnabled(False)
        self.pushButton_Salir.setGeometry(QtCore.QRect(70, 390, 141, 51))
        font = QtGui.QFont()
        self.pushButton_Salir.setFont(font)
        self.pushButton_Salir.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,   \n"
                "                                       stop: 0 rgba(186, 85, 211, 255), /* Violeta claro */\n"
                "                                       stop: 1 rgba(169, 169, 169, 255)); /* Gris suave */\n"
                "    color: rgba(255, 255, 255, 240); /* Texto blanco */\n"
                "    border: none;  \n"
                "    padding: 12px 20px;  \n"
                "    border-radius: 5px;  \n"
                "\n"
                "    text-transform: uppercase; \n"
                "    cursor: pointer;\n"
                "    transition: background-color 0.3s ease, transform 0.2s ease; /* Transiciones suaves */")
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(70, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(19)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 61, 61))
        self.label_6.setStyleSheet("border-image: url(:/imagenes/3709737-call-centre-online-service-support_108089.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 61, 61))
        self.label_7.setStyleSheet("border-image: url(:/imagenes/content_design_pencil_edit_windows_icon_193926.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        Window_opciones.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_opciones)
        QtCore.QMetaObject.connectSlotsByName(Window_opciones)

    def retranslateUi(self, Window_opciones):
        _translate = QtCore.QCoreApplication.translate
        Window_opciones.setWindowTitle(_translate("Window_opciones", "MainWindow"))
        self.label_4.setText(_translate("Window_opciones", "MENU PASSKEEPER"))
        self.pushButton_RegistarNuevoServicio.setText(_translate("Window_opciones", "Registrar nuevo servicio"))
        self.pushButton_VerlistaDeservivios.setText(_translate("Window_opciones", "Ver lista de servicios"))
        self.pushButton_Salir.setText(_translate("Window_opciones", "SALIR"))
        self.label_5.setText(_translate("Window_opciones", "ELIJE UNA OPCCION"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_opciones = QtWidgets.QMainWindow()
    ui = Ui_Window_opciones()
    ui.setupUi(Window_opciones)
    Window_opciones.show()
    sys.exit(app.exec_())