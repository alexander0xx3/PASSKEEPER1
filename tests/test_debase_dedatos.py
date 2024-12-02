import unittest
from Logica.BaseDeDatos import BaseDeDatos
import random
import string

class TestBaseDeDatos(unittest.TestCase):

    def setUp(self):

        self.db = BaseDeDatos()

    def generar_aleatorio(self, longitud=8):

        return ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))

    def test_guardar_servicio(self):


        # Generamos datos aleatorios
        usuario = self.generar_aleatorio()
        contrasena = self.generar_aleatorio(12)
        servicio = self.generar_aleatorio(10)


        try:
            self.db.guardar_servicio(usuario, contrasena, servicio)

            # Comprobamos si los datos han sido guardados correctamente en la base de datos
            # Aquí puedes hacer una consulta a la base de datos para verificar que los datos están presentes
            cursor = self.db.conn.cursor()
            cursor.execute('SELECT * FROM servicios WHERE usuario=? AND servicio=?', (usuario, servicio))
            result = cursor.fetchone()

            # Verificamos que el resultado no sea None (lo que significa que se encontraron datos)
            self.assertIsNotNone(result, f"El servicio {servicio} no fue guardado correctamente.")
            print(f"Datos guardados correctamente: {result}")

        except Exception as e:
            self.fail(f"Error al guardar el servicio: {str(e)}")

    def tearDown(self):

        # Opcional: Eliminar registros de prueba para limpiar la base de datos (si es necesario)
        cursor = self.db.conn.cursor()
        cursor.execute('DELETE FROM servicios')
        self.db.conn.commit()

if __name__ == "__main__":
    unittest.main()