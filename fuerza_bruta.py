# fuerza_bruta.py

import time

# Contraseña correcta simulada
contraseña_correcta = "admin123"

# Leer contraseñas desde archivo
with open("diccionario.txt", "r") as archivo:
    contraseñas = archivo.read().splitlines()

# Intentar cada contraseña
for intento in contraseñas:
    print(f"Probando: {intento}")
    time.sleep(0.3)
    if intento == contraseña_correcta:
        print(f"✅ Contraseña encontrada: {intento}")
        break
else:
    print("❌ Contraseña no encontrada.")
