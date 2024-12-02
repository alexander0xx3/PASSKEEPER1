import pytest
import unittest
import os
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication
from Logica.VentanaLogin import VentanaLogin
from Logica.VentanaOpciones import VentanaOpciones


class TestIntegracionLogin(unittest.TestCase):
    """Pruebas de integración para el flujo de login"""

    @classmethod
    def setUpClass(cls):
        """Configuración inicial para todas las pruebas de la clase"""
        # Asegurar que solo hay una instancia de QApplication
        if not QApplication.instance():
            cls.app = QApplication([])
        else:
            cls.app = QApplication.instance()

        # Configurar base de datos de prueba
        cls.test_db = 'test_usuarios.db'

    def setUp(self):
        """Configuración inicial para cada test"""
        # Crear nueva conexión para cada test
        self.ventana_login = VentanaLogin()
        self.ventana_login.conn = sqlite3.connect(self.test_db)
        self.ventana_login.cursor = self.ventana_login.conn.cursor()

        # Crear tabla de prueba
        self.ventana_login.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                contrasena TEXT NOT NULL
            )
        ''')
        self.ventana_login.conn.commit()

    def tearDown(self):
        """Limpieza después de cada test"""
        # Cerrar conexiones y limpiar
        if hasattr(self, 'ventana_login'):
            self.ventana_login.conn.close()
            self.ventana_login.close()

        # Procesar eventos pendientes
        QApplication.processEvents()

        # Eliminar archivo de base de datos
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError:
                pass

    @classmethod
    def tearDownClass(cls):
        """Limpieza final después de todas las pruebas"""
        # Cerrar todas las ventanas
        for widget in QApplication.topLevelWidgets():
            widget.close()

        # Procesar eventos pendientes
        QApplication.processEvents()

    def test_flujo_registro_login(self):
        """Prueba el flujo completo de registro y login"""
        try:
            # Registro de usuario
            self.ventana_login.lineEdit_usuario.setText("test_integration")
            self.ventana_login.lineEdit_contrasena.setText("test_pass")
            QTest.mouseClick(self.ventana_login.pushButton_registrarse, Qt.LeftButton)
            QApplication.processEvents()

            # Verificar registro exitoso
            self.ventana_login.cursor.execute('SELECT * FROM usuarios WHERE usuario = ?', ("test_integration",))
            self.assertIsNotNone(self.ventana_login.cursor.fetchone())

            # Login con el usuario registrado
            self.ventana_login.lineEdit_usuario.setText("test_integration")
            self.ventana_login.lineEdit_contrasena.setText("test_pass")
            QTest.mouseClick(self.ventana_login.pushButton_iniciarSesion, Qt.LeftButton)
            QApplication.processEvents()

            # Dar tiempo para que se procesen los eventos
            QApplication.processEvents()

            # Verificar que se abre la ventana de opciones
            ventanas_opciones = [w for w in QApplication.topLevelWidgets()
                                 if isinstance(w, VentanaOpciones)]
            self.assertTrue(len(ventanas_opciones) > 0)

        except Exception as e:
            self.fail(f"Test falló con error: {str(e)}")
        finally:
            # Asegurar limpieza
            for widget in QApplication.topLevelWidgets():
                widget.close()
            QApplication.processEvents()