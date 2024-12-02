import pyautogui
import time

# Espera inicial para lanzar la aplicación manualmente si es necesario
print("Inicia la aplicación antes de comenzar. Esperando 5 segundos...")
time.sleep(5)

# ---------------------
# FUNCIONES AUXILIARES
# ---------------------

def esperar_segundos(segundos, mensaje=""):
    """Espera con mensaje opcional."""
    if mensaje:
        print(mensaje)
    time.sleep(segundos)

def escribir_campo(x, y, texto):
    """Haz clic en el campo y escribe texto."""
    pyautogui.click(x, y)
    pyautogui.typewrite(texto)
    esperar_segundos(1, f"Escribiendo '{texto}' en el campo...")

def hacer_clic(x, y, mensaje=""):
    """Haz clic en una posición."""
    pyautogui.click(x, y)
    if mensaje:
        print(mensaje)
    esperar_segundos(1)

# ---------------------
# FLUJO DE SIMULACIÓN
# ---------------------

# 1. Registrar un nuevo usuario
print("Simulando registro de un usuario...")
escribir_campo(400, 250, "usuario_prueba")  # Coordenadas del campo "Usuario"
escribir_campo(400, 320, "contraseña123")  # Coordenadas del campo "Contraseña"
hacer_clic(400, 400, "Registrando usuario...")  # Coordenadas del botón "Registrar"

# 2. Iniciar sesión con el nuevo usuario
print("Simulando inicio de sesión...")
escribir_campo(400, 250, "usuario_prueba")  # Campo "Usuario"
escribir_campo(400, 320, "contraseña123")  # Campo "Contraseña"
hacer_clic(400, 400, "Iniciando sesión...")  # Botón "Iniciar Sesión"

# 3. Navegar al menú principal
print("Navegando al menú principal...")
esperar_segundos(3, "Esperando que cargue el menú...")

# 4. Registrar un nuevo servicio
print("Simulando registro de un servicio...")
hacer_clic(200, 200, "Accediendo a la ventana 'Registrar Servicio'...")  # Botón para abrir ventana
esperar_segundos(2)

escribir_campo(400, 250, "usuario_servicio")  # Campo "Usuario Servicio"
escribir_campo(400, 320, "contraseña_servicio")  # Campo "Contraseña Servicio"
escribir_campo(400, 380, "mi_servicio")  # Campo "Servicio"
hacer_clic(400, 450, "Guardando servicio...")  # Botón "Guardar Servicio"

# 5. Ver la lista de servicios
print("Simulando visualización de la lista de servicios...")
hacer_clic(200, 300, "Accediendo a la lista de servicios...")  # Botón para abrir ventana
esperar_segundos(3)

# 6. Editar un servicio
print("Simulando edición de un servicio...")
hacer_clic(200, 250, "Seleccionando un servicio para editar...")  # Selección en tabla
hacer_clic(300, 350, "Abriendo ventana de edición...")  # Botón "Editar"
esperar_segundos(2)

escribir_campo(400, 250, "usuario_actualizado")  # Editar "Usuario"
escribir_campo(400, 320, "contraseña_actualizada")  # Editar "Contraseña"
hacer_clic(400, 450, "Actualizando servicio...")  # Botón "Actualizar"

# 7. Cerrar sesión
print("Simulando cierre de sesión...")
hacer_clic(200, 400, "Cerrando sesión...")  # Botón "Salir"
esperar_segundos(2)

print("Simulación completa.")

# ---------------------
# NOTAS IMPORTANTES
# ---------------------
# - Cambia las coordenadas (x, y) según tu pantalla con pyautogui.position().
# - Asegúrate de que la interfaz esté en el lugar esperado para cada paso.
# - Usa pyautogui.screenshot() para guardar capturas en cada paso, si es necesario.
