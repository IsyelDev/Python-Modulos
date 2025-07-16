from io import open

# Escribir texto inicial
texto = "Tanjiru MOMENTOS DIVERTIDOS Kimetsu No YAIBA Audio Latino TEMPORADA 2 E1"
with open("fichero.txt", "w", encoding="utf-8") as f:
    f.write(texto)

# Leer el contenido
with open("fichero.txt", "r+", encoding="utf-8") as f:
    lineas = f.readlines()
    print("Contenido original:", lineas)

# Agregar texto al final
with open("fichero.txt", "a", encoding="utf-8") as f:
    f.write("\nHola, ¿cómo estás?")

# Ver resultado final
with open("fichero.txt", "r", encoding="utf-8") as f:
    print("Contenido actualizado:", f.read())

# Leer otro archivo (con verificación de existencia)
import os
if os.path.exists("fichero2.txt"):
    with open("fichero2.txt", "r", encoding="utf-8") as f2:
        print("Contenido de fichero2.txt:", f2.read())
else:
    print("fichero2.txt no existe.")
