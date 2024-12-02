import unittest
import os
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from Logica.BaseDeDatos import BaseDeDatos
from Logica.Ventana_RegistrarServicio import VentanaRegistrarServicio
from Logica.VentanaEditar import VentanaEditar
from Logica.VentanaListaDeservicios import VentanaListaDeservicios
from Logica.res_rc import res_rc

class TestIntegracionServicios(unittest.TestCase):
    """Pruebas de integración para el flujo de servicios"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.test_db = 'test_servicios.db'
        self.db = BaseDeDatos()
        self.db.conn = sqlite3.connect(self.test_db)
        self.db.cursor = self.db.conn.cursor()

        # Crear tabla de prueba
        self.db.cursor.execute('''
            CREATE TABLE IF NOT EXISTS servicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                contrasena TEXT NOT NULL,
                servicio TEXT NOT NULL
            )
        ''')
        self.db.conn.commit()

    def tearDown(self):
        """Limpieza después de cada test"""
        self.db.conn.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_flujo_crud_servicio(self):
        """Prueba el flujo completo CRUD de un servicio"""
        # Crear servicio
        ventana_registro = VentanaRegistrarServicio()
        ventana_registro.db = self.db
        ventana_registro.ui.lineEdit_usuario.setText("user_test")
        ventana_registro.ui.lineEdit_contrasena.setText("pass_test")
        ventana_registro.ui.lineEdit_servicio.setText("service_test")
        ventana_registro.guardar_servicio()

        # Verificar creación
        self.db.cursor.execute('SELECT * FROM servicios WHERE usuario = ?', ("user_test",))
        servicio_creado = self.db.cursor.fetchone()
        self.assertIsNotNone(servicio_creado)

        # Editar servicio
        ventana_editar = VentanaEditar(servicio_creado[0])
        ventana_editar.db = self.db
        ventana_editar.ui.lineEdit_usuarioActualizar.setText("user_edited")
        ventana_editar.ui.lineEdit_contrasenaActualizar.setText("pass_edited")
        ventana_editar.ui.lineEdit_servicioActualizar.setText("service_edited")
        ventana_editar.actualizar_servicio()

        # Verificar edición
        self.db.cursor.execute('SELECT * FROM servicios WHERE id = ?', (servicio_creado[0],))
        servicio_editado = self.db.cursor.fetchone()
        self.assertEqual(servicio_editado[1], "user_edited")

        # Verificar lista de servicios
        ventana_lista = VentanaListaDeservicios()
        ventana_lista.db = self.db
        ventana_lista.cargar_servicios()
        self.assertEqual(ventana_lista.ui.tableWidget.rowCount(), 1)

        # Eliminar servicio
        ventana_lista.servicio_seleccionado = 0
        ventana_lista.eliminar_servicio()

        # Verificar eliminación
        self.db.cursor.execute('SELECT * FROM servicios WHERE id = ?', (servicio_creado[0],))
        self.assertIsNone(self.db.cursor.fetchone())