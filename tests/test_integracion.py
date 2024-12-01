import unittest
from PyQt5.QtWidgets import QApplication
import sys
from Logica import VentanaLogin
from Logica.VentanaOpciones import VentanaOpciones
from Logica.BaseDeDatos import BaseDeDatos


class TestIntegracion(unittest.TestCase):
    """Pruebas de integración entre componentes"""

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.db = BaseDeDatos()

    def test_flujo_login_opciones(self):
        """Prueba el flujo completo desde login hasta opciones"""
        # Crear usuario de prueba
        login = VentanaLogin()
        login.lineEdit_usuario.setText("test_integration")
        login.lineEdit_contrasena.setText("test_pass")
        login.mostrar_registro()

        # Intentar login
        login.lineEdit_usuario.setText("test_integration")
        login.lineEdit_contrasena.setText("test_pass")
        login.iniciar_sesion()

        # Verificar que se abrió la ventana de opciones
        ventanas_opciones = [w for w in QApplication.topLevelWidgets()
                             if isinstance(w, VentanaOpciones)]
        self.assertEqual(len(ventanas_opciones), 1)

    def test_flujo_completo_servicio(self):
        """Prueba el flujo completo de crear, editar y eliminar un servicio"""
        from Logica.Ventana_RegistrarServicio import VentanaRegistrarServicio
        from Logica.VentanaEditar import VentanaEditar

        # Registrar nuevo servicio
        registro = VentanaRegistrarServicio()
        registro.ui.lineEdit_usuario.setText("user_flow")
        registro.ui.lineEdit_contrasena.setText("pass_flow")
        registro.ui.lineEdit_servicio.setText("service_flow")
        registro.guardar_servicio()

        # Verificar que se guardó
        servicios = self.db.obtener_servicios()
        servicio_creado = next((s for s in servicios if s[1] == "user_flow"), None)
        self.assertIsNotNone(servicio_creado)

        # Editar servicio
        id_servicio = servicio_creado[0]
        editar = VentanaEditar(id_servicio)
        editar.ui.lineEdit_usuarioActualizar.setText("user_flow_edited")
        editar.ui.lineEdit_contrasenaActualizar.setText("pass_flow_edited")
        editar.ui.lineEdit_servicioActualizar.setText("service_flow_edited")
        editar.actualizar_servicio()

        # Verificar edición
        servicios = self.db.obtener_servicios()
        servicio_editado = next((s for s in servicios if s[0] == id_servicio), None)
        self.assertEqual(servicio_editado[1], "user_flow_edited")

        # Eliminar servicio
        self.db.eliminar_servicio(id_servicio)

        # Verificar eliminación
        servicios = self.db.obtener_servicios()
        servicio_eliminado = next((s for s in servicios if s[0] == id_servicio), None)
        self.assertIsNone(servicio_eliminado)


if __name__ == '__main__':
    unittest.main()