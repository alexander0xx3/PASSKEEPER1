import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from Logica.VentanaOpciones import VentanaOpciones  # Asegúrate de que la ruta sea correcta

class TestVentanaOpcionesFuncionalidad(unittest.TestCase):

    def setUp(self):
        """Configuración previa a cada prueba."""
        self.app = QApplication(sys.argv)
        self.window = VentanaOpciones()
        self.window.ui.pushButton_RegistarNuevoServicio.setFocusPolicy(Qt.StrongFocus)
        self.window.ui.pushButton_VerlistaDeservivios.setFocusPolicy(Qt.StrongFocus)
        self.window.ui.pushButton_Salir.setFocusPolicy(Qt.StrongFocus)
        self.window.show()
        QTest.qWait(800)  # Asegurarse de que la ventana esté visible

    def tearDown(self):
        """Limpieza después de cada prueba."""
        self.window.close()

    def test_focus_on_buttons(self):
        """Verificar que los botones puedan recibir foco."""
        self.window.ui.pushButton_RegistarNuevoServicio.setFocus()
        QTest.qWait(800)
        self.assertTrue(self.window.ui.pushButton_RegistarNuevoServicio.hasFocus())

        self.window.ui.pushButton_VerlistaDeservivios.setFocus()
        QTest.qWait(800)
        self.assertTrue(self.window.ui.pushButton_VerlistaDeservivios.hasFocus())

        self.window.ui.pushButton_Salir.setFocus()
        QTest.qWait(800)
        self.assertTrue(self.window.ui.pushButton_Salir.hasFocus())

if __name__ == '__main__':
    unittest.main()