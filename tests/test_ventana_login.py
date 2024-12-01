import unittest
from PyQt5.QtWidgets import QApplication
import sys
from Logica.VentanaLogin import VentanaLogin
from Logica.VentanaOpciones import VentanaOpciones
from Logica.BaseDeDatos import BaseDeDatos


class TestIntegracion(unittest.TestCase):
    """Pruebas de integración entre componentes"""

    @classmethod
    def setUpClass(cls):
        """Configuración inicial que se ejecuta una vez antes de todas las pruebas."""
        cls.app = QApplication(sys.argv)
        cls.db = BaseDeDatos()  # La tabla se crea automáticamente en el constructor

    @classmethod
    def tearDownClass(cls):
        """Limpieza final que se ejecuta una vez después de todas las pruebas."""
        cls.db.cursor.execute('DELETE FROM servicios')  # Limpia todos los datos de la tabla
        cls.db.conn.commit()
        cls.db.conn.close()

    def test_flujo_login_opciones(self):
        """Prueba el flujo completo desde login hasta opciones."""
        # Crear usuario de prueba en el sistema
        login = VentanaLogin()
        login.lineEdit_usuario.setText("test_integration")
        login.lineEdit_contrasena.setText("test_pass")
        login.mostrar_registro()

        # Intentar iniciar sesión con las credenciales registradas
        login.lineEdit_usuario.setText("test_integration")
        login.lineEdit_contrasena.setText("test_pass")
        login.iniciar_sesion()

        # Verificar que se abrió la ventana de opciones
        ventanas_opciones = [
            widget for widget in QApplication.topLevelWidgets()
            if isinstance(widget, VentanaOpciones)
        ]
        self.assertEqual(len(ventanas_opciones), 1, "No se abrió la ventana de opciones.")

    def test_flujo_completo_servicio(self):
        """Prueba el flujo completo de crear, editar y eliminar un servicio."""
        from Logica.Ventana_RegistrarServicio import VentanaRegistrarServicio
        from Logica.VentanaEditar import VentanaEditar

        # Registrar un nuevo servicio
        registro = VentanaRegistrarServicio()
        registro.ui.lineEdit_usuario.setText("user_flow")
        registro.ui.lineEdit_contrasena.setText("pass_flow")
        registro.ui.lineEdit_servicio.setText("service_flow")
        registro.guardar_servicio()

        # Verificar que el servicio se haya guardado
        servicios = self.db.obtener_servicios()
        servicio_creado = next((s for s in servicios if s[1] == "user_flow"), None)
        self.assertIsNotNone(servicio_creado, "El servicio no se registró correctamente.")

        # Editar el servicio
        id_servicio = servicio_creado[0]
        editar = VentanaEditar(id_servicio)
        editar.ui.lineEdit_usuarioActualizar.setText("user_flow_edited")
        editar.ui.lineEdit_contrasenaActualizar.setText("pass_flow_edited")
        editar.ui.lineEdit_servicioActualizar.setText("service_flow_edited")
        editar.actualizar_servicio()

        # Verificar que la edición fue exitosa
        servicios = self.db.obtener_servicios()
        servicio_editado = next((s for s in servicios if s[0] == id_servicio), None)
        self.assertIsNotNone(servicio_editado, "El servicio no se encontró después de editarlo.")
        self.assertEqual(servicio_editado[1], "user_flow_edited", "El servicio no se actualizó correctamente.")

        # Eliminar el servicio
        self.db.eliminar_servicio(id_servicio)

        # Verificar que el servicio fue eliminado
        servicios = self.db.obtener_servicios()
        servicio_eliminado = next((s for s in servicios if s[0] == id_servicio), None)
        self.assertIsNone(servicio_eliminado, "El servicio no se eliminó correctamente.")



if __name__ == '__main__':
    unittest.main()