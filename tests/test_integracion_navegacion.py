import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import sqlite3
import os
from Logica.VentanaListaDeservicios import VentanaListaDeservicios

class TestVentanaListaServicios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        # Create test database
        cls.test_db = 'test_servicios.db'
        cls.conn = sqlite3.connect(cls.test_db)
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS servicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                contrasena TEXT NOT NULL,
                servicio TEXT NOT NULL
            )
        ''')
        cls.conn.commit()

    def setUp(self):
        self.ventana = VentanaListaDeservicios()
        # Insertar datos de prueba
        self.cursor.execute('''
            INSERT INTO servicios (usuario, contrasena, servicio)
            VALUES (?, ?, ?)
        ''', ('test_user', 'test_pass', 'test_service'))
        self.conn.commit()

    def tearDown(self):
        self.ventana.close()
        self.cursor.execute('DELETE FROM servicios')
        self.conn.commit()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove(cls.test_db)
        cls.app.quit()

    def test_cargar_servicios(self):
        # Verificar que los servicios se cargan correctamente
        self.ventana.cargar_servicios()
        self.assertEqual(self.ventana.ui.tableWidget.rowCount(), 1)

    def test_seleccionar_servicio(self):
        # Test selección de servicio
        self.ventana.cargar_servicios()
        self.ventana.ui.tableWidget.selectRow(0)
        self.assertEqual(self.ventana.servicio_seleccionado, 0)

    def test_eliminar_servicio(self):
        # Test eliminación de servicio
        self.ventana.cargar_servicios()
        self.ventana.ui.tableWidget.selectRow(0)
        QTest.mouseClick(self.ventana.ui.pushButton_eliminar, Qt.LeftButton)
        # Verificar que el servicio se eliminó

    def test_desencriptar_contrasena(self):
        # Test desencriptación de contraseña
        self.ventana.cargar_servicios()
        self.ventana.ui.tableWidget.selectRow(0)
        QTest.mouseClick(self.ventana.ui.pushButton_desencriptar, Qt.LeftButton)
        # Verificar que la contraseña se muestra correctamente