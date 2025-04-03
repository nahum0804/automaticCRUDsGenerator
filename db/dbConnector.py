import psycopg2
import json

class PostgresDB:
    def __init__(self, credenciales_path):
        self.credenciales_path = credenciales_path
        self.conexion = None

    def conectar(self):
        """Establece la conexión con la base de datos."""
        try:
            with open(self.credenciales_path) as archivo:
                credenciales = json.load(archivo)
            
            self.conexion = psycopg2.connect(**credenciales)
            print("Conexión exitosa a PostgreSQL")
        except psycopg2.Error as e:
            print("Ocurrió un error al conectar a PostgreSQL:", e)
            self.conexion = None

    def cerrar_conexion(self):
        """Cierra la conexión si está abierta."""
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada correctamente")

    def ejecutar_consulta(self, consulta, parametros=None):
        """Ejecuta una consulta SQL y devuelve los resultados si aplica."""
        if not self.conexion:
            print("No hay conexión establecida.")
            return None
        
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, parametros)
                if consulta.strip().lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    self.conexion.commit()
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)
            return None
