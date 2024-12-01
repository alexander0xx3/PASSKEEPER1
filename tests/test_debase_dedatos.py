import sys
import os
import unittest
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

# Asegurar que la carpeta 'Logica' esté en el sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Logica')))

from Logica.VentanaOpciones import VentanaOpciones  # Importar la clase correctamente

class TestVentanaOpciones(unittest.TestCase):

    def setUp(self):
        """Configuración previa a cada prueba."""
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
        self.window = VentanaOpciones()  # Ventana que deseas probar
        self.window.show()

    def tearDown(self):
        """Limpiar después de cada prueba."""
        if self.window:
            self.window.close()
            self.window.deleteLater()
        if self.app:
            self.app.quit()

    def test_initial_window(self):
        """Verificar que la ventana se inicializa correctamente y está visible."""
        self.assertTrue(self.window.isVisible())

    def test_button_enablement(self):
        """Verificar que los botones están habilitados al inicio."""
        self.assertTrue(self.window.ui.pushButton_RegistarNuevoServicio.isEnabled())
        self.assertTrue(self.window.ui.pushButton_VerlistaDeservivios.isEnabled())
        self.assertTrue(self.window.ui.pushButton_Salir.isEnabled())

    def test_button_register_new_service(self):
        """Verificar que al hacer clic en 'Registrar nuevo servicio' se abre la ventana correspondiente."""
        QTest.mouseClick(self.window.ui.pushButton_RegistarNuevoServicio, Qt.LeftButton)

        from Logica.Ventana_RegistrarServicio import VentanaRegistrarServicio
        self.assertIsInstance(self.window.ventana_registro, VentanaRegistrarServicio)
        self.assertTrue(self.window.ventana_registro.isVisible())

    def test_button_view_service_list(self):
        """Verificar que al hacer clic en 'Ver lista de servicios' se abre la ventana correspondiente."""
        QTest.mouseClick(self.window.ui.pushButton_VerlistaDeservivios, Qt.LeftButton)

        from Logica.VentanaListaDeservicios import VentanaListaDeservicios
        self.assertIsInstance(self.window.ventana_lista, VentanaListaDeservicios)
        self.assertTrue(self.window.ventana_lista.isVisible())

    def test_button_exit(self):
        """Verificar que al hacer clic en 'Salir' se cierra la ventana y vuelve al login."""
        QTest.mouseClick(self.window.ui.pushButton_Salir, Qt.LeftButton)
        self.assertFalse(self.window.isVisible())

        from Logica.VentanaLogin import VentanaLogin
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, VentanaLogin):
                self.assertTrue(widget.isVisible())
                break


if __name__ == '__main__':
    unittest.main()