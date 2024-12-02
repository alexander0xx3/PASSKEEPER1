from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BaseDeDatos import BaseDeDatos


class VentanaEditar(QtWidgets.QMainWindow):
    def __init__(self, id_servicio):
        super(VentanaEditar, self).__init__()
        self.ui = Ui_Window_Editar()
        self.ui.setupUi(self)

        # Configurar ventana sin bordes
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.db = BaseDeDatos()
        self.id_servicio = id_servicio
        self.cargar_datos_servicio()

        # Configurar el modo de contraseña
        self.ui.lineEdit_contrasenaActualizar.setEchoMode(QtWidgets.QLineEdit.Password)

        # Conectar el botón "Actualizar"
        self.ui.pushButton_Actualizar.clicked.connect(self.actualizar_servicio)

    def cargar_datos_servicio(self):
        servicios = self.db.obtener_servicios()
        servicio = servicios[self.id_servicio]

        self.ui.lineEdit_usuarioActualizar.setText(servicio[1])
        self.ui.lineEdit_servicioActualizar.setText(servicio[3])

    def actualizar_servicio(self):
        usuario = self.ui.lineEdit_usuarioActualizar.text()
        contrasena = self.ui.lineEdit_contrasenaActualizar.text()
        servicio = self.ui.lineEdit_servicioActualizar.text()

        if not usuario or not contrasena or not servicio:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")
            return

        try:
            servicios = self.db.obtener_servicios()
            id_servicio = servicios[self.id_servicio][0]
            self.db.actualizar_servicio(id_servicio, usuario, contrasena, servicio)
            QMessageBox.information(self, "Éxito", "Servicio actualizado correctamente")
            self.volver_a_lista()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al actualizar el servicio: {str(e)}")

    def volver_a_lista(self):
        from VentanaListaDeservicios import VentanaListaDeservicios
        self.ventana_lista = VentanaListaDeservicios()
        self.ventana_lista.cargar_servicios()
        self.ventana_lista.show()
        self.close()



class Ui_Window_Editar(object):
    def setupUi(self, Window_Editar):
        Window_Editar.setObjectName("Window_Editar")
        Window_Editar.resize(491, 430)
        self.centralwidget = QtWidgets.QWidget(Window_Editar)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 491, 431))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 231, 431))
        self.label_3.setStyleSheet("border-image: url(:/imagenes/chill_guy_meme_iphone_anime_hd_4k_paisajes_naturales_y_atardecer_arte.jpg);\n"
            "\n"
            "\n"
            "\n"
            "background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
            "    border-bottom-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
            "  border-up-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
            "    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
            "    padding: 20px; \n"
            "border-top-left-radius: 50px;\n"
            "                     border: 1px solid #ccc;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(210, 0, 281, 431))
        self.label_4.setStyleSheet("\n"
                "\n"
                "background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
                "    border-bottom-right-radius: 70px; /* Esquina inferior derecha redondeada */  \n"
                "    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
                "    padding: 20px; \n"
                "\n"
                "\n"
                "border-top-right-radius: 50px;\n"
                "                     border: 1px solid #ccc;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_contrasenaActualizar = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_contrasenaActualizar.setGeometry(QtCore.QRect(260, 220, 195, 40))
        self.lineEdit_contrasenaActualizar.setStyleSheet("\n"
                "    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
                "    border: none; /* Sin borde por defecto */  \n"
                "    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
                "    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
                "    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
                "")
        self.lineEdit_contrasenaActualizar.setText("")
        self.lineEdit_contrasenaActualizar.setObjectName("lineEdit_contrasenaActualizar")
        self.lineEdit_usuarioActualizar = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_usuarioActualizar.setGeometry(QtCore.QRect(260, 170, 195, 40))
        self.lineEdit_usuarioActualizar.setStyleSheet("\n"
                "    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
                "    border: none; /* Sin borde por defecto */  \n"
                "    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
                "    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
                "    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
                "")
        self.lineEdit_usuarioActualizar.setObjectName("lineEdit_usuarioActualizar")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(250, 50, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_Actualizar = QtWidgets.QPushButton(self.widget)
        self.pushButton_Actualizar.setGeometry(QtCore.QRect(270, 350, 151, 41))
        self.pushButton_Actualizar.setStyleSheet(" background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,    \n"
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
        self.pushButton_Actualizar.setAutoDefault(False)
        self.pushButton_Actualizar.setObjectName("pushButton_Actualizar")
        self.lineEdit_servicioActualizar = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_servicioActualizar.setGeometry(QtCore.QRect(260, 280, 195, 40))
        self.lineEdit_servicioActualizar.setStyleSheet("\n"
                "    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
                "    border: none; /* Sin borde por defecto */  \n"
                "    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
                "    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
                "    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
                "")
        self.lineEdit_servicioActualizar.setText("")
        self.lineEdit_servicioActualizar.setObjectName("lineEdit_servicioActualizar")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(220, 0, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(210, 120, 281, 31))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:rgba(0,0,0,75);\n"
"")
        self.label_11.setObjectName("label_11")
        Window_Editar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_Editar)
        QtCore.QMetaObject.connectSlotsByName(Window_Editar)

    def retranslateUi(self, Window_Editar):
        _translate = QtCore.QCoreApplication.translate
        Window_Editar.setWindowTitle(_translate("Window_Editar", "MainWindow"))
        self.lineEdit_contrasenaActualizar.setPlaceholderText(_translate("Window_Editar", "  CONTRASEÑA"))
        self.lineEdit_usuarioActualizar.setPlaceholderText(_translate("Window_Editar", "  USUARIO"))
        self.label_9.setText(_translate("Window_Editar", "SERVICIO"))
        self.pushButton_Actualizar.setText(_translate("Window_Editar", "ACTUALIZAR"))
        self.lineEdit_servicioActualizar.setPlaceholderText(_translate("Window_Editar", "  SERVICIO"))
        self.label_10.setText(_translate("Window_Editar", "ACTUALIZAR"))
        self.label_11.setText(_translate("Window_Editar", "ACTUALIZE SUS DATOS"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_Editar = QtWidgets.QMainWindow()
    ui = Ui_Window_Editar()
    ui.setupUi(Window_Editar)
    Window_Editar.show()
    sys.exit(app.exec_())
