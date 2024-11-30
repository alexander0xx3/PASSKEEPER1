from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BaseDeDatos import BaseDeDatos

class VentanaRegistrarServicio(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaRegistrarServicio, self).__init__()
        self.ui = Ui_Window_RegistrarServicio()
        self.ui.setupUi(self)

        # Configurar ventana sin bordes
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.db = BaseDeDatos()
        self.conectar_botones()

        # Configurar el modo de contraseña
        self.ui.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)

    def conectar_botones(self):
        self.ui.pushButton_guardar.clicked.connect(self.guardar_servicio)

    def guardar_servicio(self):
        usuario = self.ui.lineEdit_usuario.text()
        contrasena = self.ui.lineEdit_contrasena.text()
        servicio = self.ui.lineEdit_servicio.text()

        if not usuario or not contrasena or not servicio:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")
            return

        try:
            self.db.guardar_servicio(usuario, contrasena, servicio)
            QMessageBox.information(self, "Éxito", "Servicio guardado correctamente")
            self.limpiar_campos()

            # Cerrar la ventana actual y regresar a la anterior
            self.close()
            # Buscar la ventana de opciones y mostrarla
            for widget in QtWidgets.QApplication.topLevelWidgets():
                if isinstance(widget, QtWidgets.QMainWindow) and widget.__class__.__name__ == 'VentanaOpciones':
                    widget.show()
                    break
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al guardar el servicio: {str(e)}")

    def limpiar_campos(self):
        self.ui.lineEdit_usuario.clear()
        self.ui.lineEdit_contrasena.clear()
        self.ui.lineEdit_servicio.clear()


class Ui_Window_RegistrarServicio(object):
    def setupUi(self, Window_RegistrarServicio):
        Window_RegistrarServicio.setObjectName("Window_RegistrarServicio")
        Window_RegistrarServicio.resize(492, 433)
        self.centralwidget = QtWidgets.QWidget(Window_RegistrarServicio)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 491, 431))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 431))
        self.label.setStyleSheet("border-image: url(:/imagenes/chill_guy.jpg);\n"
"\n"
"\n"
"background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
"    border-bottom-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
"  border-up-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
"    padding: 20px; \n"
"border-top-left-radius: 50px;\n"
"                     border: 1px solid #ccc;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 281, 431))
        self.label_2.setStyleSheet("\n"
"\n"
"background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
"    border-bottom-right-radius: 70px; /* Esquina inferior derecha redondeada */  \n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
"    padding: 20px; \n"
"\n"
"\n"
"border-top-right-radius: 50px;\n"
"                     border: 1px solid #ccc;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_contrasena = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_contrasena.setGeometry(QtCore.QRect(260, 220, 195, 40))
        self.lineEdit_contrasena.setStyleSheet("\n"
"    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
"    border: none; /* Sin borde por defecto */  \n"
"    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
"    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
"    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
"")
        self.lineEdit_contrasena.setText("")
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(260, 170, 195, 40))
        self.lineEdit_usuario.setStyleSheet("\n"
"    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
"    border: none; /* Sin borde por defecto */  \n"
"    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
"    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
"    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
"")
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(250, 50, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_guardar = QtWidgets.QPushButton(self.widget)
        self.pushButton_guardar.setGeometry(QtCore.QRect(290, 350, 131, 41))
        self.pushButton_guardar.setStyleSheet(" background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,    \n"
"                                       stop: 0 rgba(255, 94, 77, 255),  /* Naranja cálido */\n"
"                                       stop: 0.5 rgba(255, 159, 64, 255), /* Amarillo suave */\n"
"                                       stop: 1 rgba(70, 130, 180, 255)); /* Azul suave del atardecer */\n"
"    color: rgba(255, 255, 255, 240); /* Texto blanco */\n"
"    border: none;  /* Sin borde */\n"
"    padding: 12px 20px;  /* Espaciado interno del botón */\n"
"    border-radius: 5px;  /* Esquinas redondeadas */\n"
"    font-size: 16px;  /* Tamaño de texto */\n"
"    font-weight: bold;  /* Texto en negrita */\n"
"    text-transform: uppercase;  /* Texto en mayúsculas */\n"
"    cursor: pointer;  /* Cursor de mano */\n"
"    transition: background-color 0.3s ease, transform 0.2s ease; /* Transición suave */\n"
"")
        self.pushButton_guardar.setAutoDefault(False)
        self.pushButton_guardar.setObjectName("pushButton_guardar")
        self.lineEdit_servicio = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_servicio.setGeometry(QtCore.QRect(260, 280, 195, 40))
        self.lineEdit_servicio.setStyleSheet("\n"
"    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
"    border: none; /* Sin borde por defecto */  \n"
"    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
"    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
"    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
"")
        self.lineEdit_servicio.setText("")
        self.lineEdit_servicio.setObjectName("lineEdit_servicio")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(250, 0, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(230, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:rgba(0,0,0,75);\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit_contrasena.raise_()
        self.lineEdit_usuario.raise_()
        self.label_6.raise_()
        self.pushButton_guardar.raise_()
        self.lineEdit_servicio.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        Window_RegistrarServicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_RegistrarServicio)
        QtCore.QMetaObject.connectSlotsByName(Window_RegistrarServicio)

    def retranslateUi(self, Window_RegistrarServicio):
        _translate = QtCore.QCoreApplication.translate
        Window_RegistrarServicio.setWindowTitle(_translate("Window_RegistrarServicio", "MainWindow"))
        self.lineEdit_contrasena.setPlaceholderText(_translate("Window_RegistrarServicio", "  CONTRASEÑA"))
        self.lineEdit_usuario.setPlaceholderText(_translate("Window_RegistrarServicio", "  USUARIO"))
        self.label_6.setText(_translate("Window_RegistrarServicio", "SERVICIO"))
        self.pushButton_guardar.setText(_translate("Window_RegistrarServicio", "GUARDAR"))
        self.lineEdit_servicio.setPlaceholderText(_translate("Window_RegistrarServicio", "  SERVICIO"))
        self.label_7.setText(_translate("Window_RegistrarServicio", "REGISTRAR"))
        self.label_8.setText(_translate("Window_RegistrarServicio", "REGISTRE SUS DATOS"))
import res_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaRegistrarServicio()
    ventana.show()
    sys.exit(app.exec_())