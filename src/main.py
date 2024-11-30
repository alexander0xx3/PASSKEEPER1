import sys
import os
from PyQt5 import QtWidgets
from VentanaLogin import VentanaLogin


def main():
    # Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Establecer la ruta base para los recursos
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # Crear y mostrar la ventana de login
    login = VentanaLogin()
    login.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()