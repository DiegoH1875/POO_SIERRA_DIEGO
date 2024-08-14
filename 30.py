import mysql.connector
from sys import exit
import os

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='escolares 2'
)

if connection.is_connected():
    print("Conexión exitosa a la base de datos MySQL")
else:
    exit("No hay conexion con la base de datos")

cursor = connection.cursor()
# Ejemplo select antes de cambios
print('TABLA DE ALUMNOS ANTES DE LOS CAMBIOS')
cursor.execute("SELECT nombre,edad FROM alumnos;")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Ejemplo de INSERT
cursor.execute("INSERT INTO alumnos (nombre, edad,direccion, maestro_id, salon_id) VALUES ('Alejandro Puentes ',20,'Por el conade', 1, 1);")

# Ejemplo de UPDATE
cursor.execute("UPDATE alumnos SET alumnos.edad = 20 WHERE alumnos.maestro_id = 6;")

# Mostrar despues de cambios
print()
print("TABLA alumnos DESPUES DE LOS CAMBIOS")
print()
cursor.execute("SELECT nombre,edad FROM alumnos;")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

connection.commit()
cursor.close()
connection.close()

