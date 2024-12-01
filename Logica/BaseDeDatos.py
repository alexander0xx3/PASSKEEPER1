import sqlite3
import hashlib

class BaseDeDatos:
    def __init__(self):
        self.conn = sqlite3.connect('servicios.db')
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS servicios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                contrasena TEXT NOT NULL,
                servicio TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def guardar_servicio(self, usuario, contrasena, servicio):
        contrasena_encriptada = self.encriptar(contrasena)
        self.cursor.execute('INSERT INTO servicios (usuario, contrasena, servicio) VALUES (?, ?, ?)',
                          (usuario, contrasena_encriptada, servicio))
        self.conn.commit()

    def obtener_servicios(self):
        self.cursor.execute('SELECT * FROM servicios')
        return self.cursor.fetchall()

    def actualizar_servicio(self, id_servicio, usuario, contrasena, servicio):
        contrasena_encriptada = self.encriptar(contrasena)
        self.cursor.execute('UPDATE servicios SET usuario=?, contrasena=?, servicio=? WHERE id=?',
                          (usuario, contrasena_encriptada, servicio, id_servicio))
        self.conn.commit()

    def eliminar_servicio(self, id_servicio):
        self.cursor.execute('DELETE FROM servicios WHERE id=?', (id_servicio,))
        self.conn.commit()

    def encriptar(self, texto):
        return hashlib.sha256(texto.encode()).hexdigest()

    def desencriptar(self, texto_encriptado):
        # En este caso, como usamos hash, no podemos desencriptar
        # Solo podemos mostrar el hash
        return texto_encriptado