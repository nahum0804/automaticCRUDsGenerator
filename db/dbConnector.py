import psycopg2
import json

with open("#") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)

try:
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)