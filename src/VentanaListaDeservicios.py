from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from BaseDeDatos import BaseDeDatos


class VentanaListaDeservicios(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaListaDeservicios, self).__init__()
        self.ui = Ui_Window_ListaDeservicios()
        self.ui.setupUi(self)

        # Configurar ventana sin bordes
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.db = BaseDeDatos()
        self.conectar_botones()
        self.cargar_servicios()
        self.servicio_seleccionado = None

    def conectar_botones(self):
        self.ui.pushButton_editar.clicked.connect(self.editar_servicio)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar_servicio)
        self.ui.pushButton_desencriptar.clicked.connect(self.desencriptar_contrasena)
        self.ui.pushButton_volver.clicked.connect(self.volver)
        self.ui.tableWidget.itemClicked.connect(self.seleccionar_servicio)

    def cargar_servicios(self):
        servicios = self.db.obtener_servicios()
        self.ui.tableWidget.setRowCount(len(servicios))

        for i, servicio in enumerate(servicios):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(servicio[1]))  # Usuario
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem('********'))  # Contraseña oculta
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(servicio[3]))  # Servicio

    def seleccionar_servicio(self, item):
        self.servicio_seleccionado = self.ui.tableWidget.currentRow()

    def editar_servicio(self):
        if self.servicio_seleccionado is None:
            QMessageBox.warning(self, "Error", "Por favor seleccione un servicio")
            return

        servicios = self.db.obtener_servicios()
        if self.servicio_seleccionado >= len(servicios):
            QMessageBox.warning(self, "Error", "Servicio no encontrado")
            return

        from VentanaEditar import VentanaEditar
        self.ventana_editar = VentanaEditar(self.servicio_seleccionado)
        self.ventana_editar.show()
        self.close()

    def eliminar_servicio(self):
        if self.servicio_seleccionado is None:
            QMessageBox.warning(self, "Error", "Por favor seleccione un servicio")
            return

        respuesta = QMessageBox.question(self, "Confirmar", "¿Está seguro de eliminar este servicio?",
                                       QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            try:
                servicios = self.db.obtener_servicios()
                id_servicio = servicios[self.servicio_seleccionado][0]
                self.db.eliminar_servicio(id_servicio)
                self.cargar_servicios()
                self.servicio_seleccionado = None
                QMessageBox.information(self, "Éxito", "Servicio eliminado correctamente")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error al eliminar el servicio: {str(e)}")

    def desencriptar_contrasena(self):
        if self.servicio_seleccionado is None:
            QMessageBox.warning(self, "Error", "Por favor seleccione un servicio")
            return

        servicios = self.db.obtener_servicios()
        contrasena = servicios[self.servicio_seleccionado][2]  # Obtener la contraseña real
        self.ui.tableWidget.setItem(self.servicio_seleccionado, 1, QTableWidgetItem(contrasena))

    def volver(self):
        from VentanaOpciones import VentanaOpciones
        self.ventana_opciones = VentanaOpciones()
        self.ventana_opciones.show()
        self.close()



class Ui_Window_ListaDeservicios(object):
    def setupUi(self, Window_ListaDeservicios):
        Window_ListaDeservicios.setObjectName("Window_ListaDeservicios")
        Window_ListaDeservicios.resize(691, 430)
        self.centralwidget = QtWidgets.QWidget(Window_ListaDeservicios)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 741, 431))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, -10, 241, 441))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
"    border-bottom-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
"  border-up-left-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
"    padding: 20px; \n"
"border-top-left-radius: 50px;\n"
"                     border: 1px solid #ccc;\n"
"\n"
"border-image: url(:/imagenes/chill_guy_meme_iphone_anime_hd_4k_paisajes_naturales_y_atardecer_art.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(240, 0, 451, 431))
        self.label_3.setStyleSheet("background-color: rgb(208, 208, 208);\n"
"\n"
"\n"
"    border-bottom-right-radius: 50px; /* Esquina inferior derecha redondeada */  \n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
"    padding: 20px; \n"
"\n"
"\n"
"border-top-right-radius: 50px;\n"
"                     border: 1px solid #ccc;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(100, 10, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(80, 80, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(320, 70, 311, 192))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 51, 61))
        self.label_2.setStyleSheet("border-image: url(:/imagenes/otros/imagenes/menu-hamburguesa.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_editar = QtWidgets.QPushButton(self.widget)
        self.pushButton_editar.setGeometry(QtCore.QRect(140, 240, 121, 41))
        self.pushButton_editar.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,  \n"
"                                       stop: 0 rgba(255, 94, 77, 255),  /* Naranja cálido */\n"
"                                       stop: 1 rgba(255, 159, 64, 255)); /* Amarillo suave */\n"
"    color: white; /* Texto blanco */\n"
"    border: none;\n"
"    padding: 12px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold; \n"
"    text-transform: uppercase;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, transform 0.2s ease; /* Transición suave */\n"
"")
        self.pushButton_editar.setAutoDefault(False)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.pushButton_eliminar = QtWidgets.QPushButton(self.widget)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(140, 300, 131, 41))
        self.pushButton_eliminar.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,  \n"
"                                       stop: 0 rgba(255, 0, 0, 255),   /* Rojo intenso */\n"
"                                       stop: 1 rgba(178, 34, 34, 255)); /* Rojo oscuro */\n"
"    color: white; /* Texto blanco */\n"
"    border: none;\n"
"    padding: 12px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, transform 0.2s ease; /* Transición suave */")
        self.pushButton_eliminar.setAutoDefault(False)
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.pushButton_desencriptar = QtWidgets.QPushButton(self.widget)
        self.pushButton_desencriptar.setGeometry(QtCore.QRect(140, 360, 141, 41))
        self.pushButton_desencriptar.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,  \n"
"                                       stop: 0 rgba(70, 130, 180, 255),  /* Azul claro */\n"
"                                       stop: 1 rgba(25, 25, 112, 255)); /* Azul oscuro */\n"
"    color: white; /* Texto blanco */\n"
"    border: none;\n"
"    padding: 12px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, transform 0.2s ease; /* Transición suave */")
        self.pushButton_desencriptar.setAutoDefault(False)
        self.pushButton_desencriptar.setObjectName("pushButton_desencriptar")
        self.pushButton_volver = QtWidgets.QPushButton(self.widget)
        self.pushButton_volver.setGeometry(QtCore.QRect(510, 370, 141, 41))
        self.pushButton_volver.setStyleSheet("   background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,  \n"
"                                       stop: 0 rgba(138, 43, 226, 255),  /* Morado */\n"
"                                       stop: 1 rgba(255, 105, 180, 255)); /* Rosa */\n"
"    color: white; /* Texto blanco */\n"
"    border: none;\n"
"    padding: 12px 20px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease, transform 0.2s ease; /* Transición suave */")
        self.pushButton_volver.setAutoDefault(False)
        self.pushButton_volver.setObjectName("pushButton_volver")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 230, 51, 61))
        self.label_4.setStyleSheet("border-image: url(:/imagenes/note-task-comment-message-edit-write_108613.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(290, 290, 51, 61))
        self.label_5.setStyleSheet("border-image: url(:/imagenes/vcsconflicting_93497.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(300, 350, 51, 61))
        self.label_6.setStyleSheet("border-image: url(:/imagenes/app_development_computer_mobile_settings_cogwheel_icon_193922.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(450, 360, 51, 61))
        self.label_7.setStyleSheet("border-image: url(:/imagenes/scienceandfiction-go_99265.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        Window_ListaDeservicios.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window_ListaDeservicios)
        QtCore.QMetaObject.connectSlotsByName(Window_ListaDeservicios)

    def retranslateUi(self, Window_ListaDeservicios):
        _translate = QtCore.QCoreApplication.translate
        Window_ListaDeservicios.setWindowTitle(_translate("Window_ListaDeservicios", "MainWindow"))
        self.label_9.setText(_translate("Window_ListaDeservicios", "LISTA DE "))
        self.label_10.setText(_translate("Window_ListaDeservicios", "SERVICIOS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Window_ListaDeservicios", "USUARIO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Window_ListaDeservicios", "CONTRASEÑA"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Window_ListaDeservicios", "SERVICIO"))
        self.pushButton_editar.setText(_translate("Window_ListaDeservicios", "EDITAR"))
        self.pushButton_eliminar.setText(_translate("Window_ListaDeservicios", "ELIMINAR"))
        self.pushButton_desencriptar.setText(_translate("Window_ListaDeservicios", "DESENCRIPTAR"))
        self.pushButton_volver.setText(_translate("Window_ListaDeservicios", "VOLVER"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_ListaDeservicios = QtWidgets.QMainWindow()
    ui = Ui_Window_ListaDeservicios()
    ui.setupUi(Window_ListaDeservicios)
    Window_ListaDeservicios.show()
    sys.exit(app.exec_())
