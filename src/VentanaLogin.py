
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import hashlib
import os


class VentanaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaLogin, self).__init__()

        # Cargar el archivo UI
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(current_dir, r'D:\Proyecto final\Ui\VentanaLogin.ui')
        uic.loadUi(ui_file, self)

        # Configurar ventana sin bordes
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # Configurar el modo de contraseña
        self.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)

        self.configurar_db()
        self.conectar_botones()

    def configurar_db(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def conectar_botones(self):
        self.pushButton_iniciarSesion.clicked.connect(self.iniciar_sesion)
        self.pushButton_registrarse.clicked.connect(self.mostrar_registro)

    def iniciar_sesion(self):
        usuario = self.lineEdit_usuario.text()
        contrasena = self.lineEdit_contrasena.text()

        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")
            return

        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

        self.cursor.execute('SELECT * FROM usuarios WHERE usuario=? AND contrasena=?',
                            (usuario, contrasena_hash))

        if self.cursor.fetchone():
            from VentanaOpciones import VentanaOpciones
            self.ventana_opciones = VentanaOpciones()
            self.ventana_opciones.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def mostrar_registro(self):
        usuario = self.lineEdit_usuario.text()
        contrasena = self.lineEdit_contrasena.text()

        if not usuario or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos")
            return

        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

        try:
            self.cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)',
                                (usuario, contrasena_hash))
            self.conn.commit()
            QMessageBox.information(self, "Éxito", "Usuario registrado correctamente")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "El usuario ya existe")

class Ui_WindowLogin(object):
    def setupUi(self, WindowLogin):
        WindowLogin.setObjectName("WindowLogin")
        WindowLogin.resize(601, 470)
        self.centralwidget = QtWidgets.QWidget(WindowLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 601, 471))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 351, 470))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
"border-image: url(:/imagenes/arbolde-sakura-en-japon-anime-zuhr2aledzyd5wso.webp);\n"
"border-top-left-radius: 50px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(310, 0, 290, 470))
        self.label_2.setStyleSheet("\n"
"\n"
"background-color: rgba(255, 255, 255, 1); /* Fondo blanco */  \n"
"    border-bottom-right-radius: 70px; /* Esquina inferior derecha redondeada */  \n"
"    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Sombra */  \n"
"    padding: 20px; ")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(330, 110, 251, 81))
        font = QtGui.QFont()
        font.setFamily("GeoSlab703 MdCn BT")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(350, 200, 195, 40))
        self.lineEdit_usuario.setStyleSheet("\n"
"    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
"    border: none; /* Sin borde por defecto */  \n"
"    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
"    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
"    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
"")
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_contrasena = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_contrasena.setGeometry(QtCore.QRect(350, 260, 195, 40))
        self.lineEdit_contrasena.setStyleSheet("\n"
"    background-color: rgba(0, 0, 0, 0); /* Fondo transparente */  \n"
"    border: none; /* Sin borde por defecto */  \n"
"    border-bottom: 2px solid rgba(46, 82, 101, 0.8); /* Borde inferior con color */  \n"
"    color: rgba(0, 0, 0, 0.94); /* Color del texto */  \n"
"    padding-bottom: 20px; /* Espacio inferior dentro del QLineEdit */  \n"
"")
        self.lineEdit_contrasena.setText("")
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.pushButton_iniciarSesion = QtWidgets.QPushButton(self.widget)
        self.pushButton_iniciarSesion.setGeometry(QtCore.QRect(390, 320, 111, 31))
        self.pushButton_iniciarSesion.setStyleSheet("\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,   \n"
"                                       stop: 0 rgba(135, 206, 250, 255),   \n"
"                                       stop: 1 rgba(70, 130, 180, 255)); /* Degradado celeste */  \n"
"    color: rgba(255, 255, 255, 240); /* Color del texto */  \n"
"    border: none; /* Sin borde */  \n"
"    padding: 10px; /* Espaciado interno del botón */  \n"
"    border-radius: 5px; /* Esquinas redondeadas (opcional) */  \n"
"\n"
"")
        self.pushButton_iniciarSesion.setAutoDefault(False)
        self.pushButton_iniciarSesion.setObjectName("pushButton_iniciarSesion")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(390, 380, 91, 16))
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_registrarse = QtWidgets.QPushButton(self.widget)
        self.pushButton_registrarse.setGeometry(QtCore.QRect(390, 400, 111, 31))
        self.pushButton_registrarse.setStyleSheet("\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,   \n"
"                                       stop: 0 rgba(144, 238, 144, 255), /* Verde claro */  \n"
"                                       stop: 1 rgba(34, 139, 34, 255)); /* Verde oscuro */  \n"
"    color: rgba(255, 255, 255, 240); /* Color del texto */  \n"
"    border: none; /* Sin borde */  \n"
"    padding: 10px; /* Espaciado interno del botón */  \n"
"    border-radius: 5px; /* Esquinas redondeadas */  \n"
"\n"
"")
        self.pushButton_registrarse.setAutoDefault(False)
        self.pushButton_registrarse.setObjectName("pushButton_registrarse")
        WindowLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(WindowLogin)
        QtCore.QMetaObject.connectSlotsByName(WindowLogin)

    def retranslateUi(self, WindowLogin):
        _translate = QtCore.QCoreApplication.translate
        WindowLogin.setWindowTitle(_translate("WindowLogin", "MainWindow"))
        self.label.setText(_translate("WindowLogin", "l"))
        self.label_3.setText(_translate("WindowLogin", "PASSKEEPER"))
        self.label_4.setText(_translate("WindowLogin", "INICIE SESION"))
        self.lineEdit_usuario.setPlaceholderText(_translate("WindowLogin", "  USUARIO"))
        self.lineEdit_contrasena.setPlaceholderText(_translate("WindowLogin", "  CONTRASEÑA"))
        self.pushButton_iniciarSesion.setText(_translate("WindowLogin", "INICIAR SESION"))
        self.label_5.setText(_translate("WindowLogin", "Nuevo usuario??"))
        self.pushButton_registrarse.setText(_translate("WindowLogin", "REGISTRARSE"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowLogin = QtWidgets.QMainWindow()
    ui = Ui_WindowLogin()
    ui.setupUi(WindowLogin)
    WindowLogin.show()
    sys.exit(app.exec_())
