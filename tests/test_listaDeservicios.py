import sys
import unittest
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from Logica.VentanaListaDeservicios import VentanaListaDeservicios

class TestVentanaListaDeservicios(unittest.TestCase):

    def setUp(self):
        """Configura el entorno antes de cada prueba."""
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
        self.window = VentanaListaDeservicios()
        self.window.show()

    def tearDown(self):
        """Limpia el entorno después de cada prueba."""
        if self.window:
            self.window.close()
            self.window.deleteLater()
        if self.app:
            self.app.quit()

    def test_initial_window(self):
        """Verifica que la ventana se inicializa correctamente."""
        self.assertTrue(self.window.isVisible())
        self.assertEqual(self.window.ui.tableWidget.rowCount(), len(self.window.db.obtener_servicios()))

    def test_select_service(self):
        """Verifica la selección de un servicio en la tabla."""
        QTest.mouseClick(self.window.ui.tableWidget.viewport(), Qt.LeftButton)
        self.window.ui.tableWidget.selectRow(0)
        self.assertEqual(self.window.servicio_seleccionado, 0)

    def test_edit_service(self):
        """Verifica que al hacer clic en 'Editar', se abre la ventana de edición."""
        self.window.servicio_seleccionado = 0
        QTest.mouseClick(self.window.ui.pushButton_editar, Qt.LeftButton)
        from Logica.VentanaEditar import VentanaEditar
        self.assertIsInstance(self.window.ventana_editar, VentanaEditar)
        self.assertTrue(self.window.ventana_editar.isVisible())

    def test_delete_service(self):
        """Simula la eliminación de un servicio y verifica que se elimina correctamente."""
        self.window.servicio_seleccionado = 0
        with unittest.mock.patch.object(QMessageBox, 'question', return_value=QMessageBox.Yes):
            QTest.mouseClick(self.window.ui.pushButton_eliminar, Qt.LeftButton)
        self.assertEqual(self.window.ui.tableWidget.rowCount(), len(self.window.db.obtener_servicios()))

    def test_decrypt_password(self):
        """Verifica que al desencriptar una contraseña, se muestra correctamente en la tabla."""
        self.window.servicio_seleccionado = 0
        QTest.mouseClick(self.window.ui.pushButton_desencriptar, Qt.LeftButton)
        servicios = self.window.db.obtener_servicios()
        self.assertEqual(self.window.ui.tableWidget.item(0, 1).text(), servicios[0][2])  # Contraseña desencriptada

    def test_return_to_options(self):
        """Verifica que al hacer clic en 'Volver', se abre la ventana de opciones."""
        QTest.mouseClick(self.window.ui.pushButton_volver, Qt.LeftButton)
        from Logica.VentanaOpciones import VentanaOpciones
        self.assertIsInstance(self.window.ventana_opciones, VentanaOpciones)
        self.assertTrue(self.window.ventana_opciones.isVisible())


if __name__ == "__main__":
    unittest.main()
