import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from Logica.VentanaLogin import VentanaLogin  # Asegúrate de que la ruta sea correcta


class TestVentanaLogin(unittest.TestCase):

    def setUp(self):
        """Configuración previa a cada prueba."""
        self.app = QApplication(sys.argv)
        self.window = VentanaLogin()

        # Accediendo directamente a los botones sin 'ui'
        self.window.pushButton_iniciarSesion.setFocusPolicy(Qt.StrongFocus)
        self.window.pushButton_registrarse.setFocusPolicy(Qt.StrongFocus)

        self.window.show()
        QTest.qWait(800)  # Asegurarse de que la ventana esté visible

    def tearDown(self):
        """Limpieza después de cada prueba."""
        self.window.close()

    def test_focus_on_buttons(self):
        """Verificar que los botones puedan recibir foco."""
        self.window.pushButton_iniciarSesion.setFocus()
        QTest.qWait(800)
        self.assertTrue(self.window.pushButton_iniciarSesion.hasFocus())

        self.window.pushButton_registrarse.setFocus()
        QTest.qWait(800)
        self.assertTrue(self.window.pushButton_registrarse.hasFocus())


if __name__ == '__main__':
    unittest.main()