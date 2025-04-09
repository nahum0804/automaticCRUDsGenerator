import psycopg2
import json
class PostgresDB:
    def __init__(self, host, user, password, database):
        # Configuración CORRECTA (claves fijas)
        self.config = {
            "host": host,        # Usa claves consistentes
            "user": user,
            "password": password,
            "database": database  # O "dbname" según psycopg2
        }

    def verificar_usuario(self, usuario, contrasena):
        """Verifica si el usuario y contraseña son válidos"""
        if not self.conexion:
            return False
            
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT verificar_usuario(%s, %s)",
                    (usuario, contrasena))
                return cursor.fetchone()[0]
        except (psycopg2.Error, TypeError) as e:
            print("Error al verificar usuario:", e)
            return False

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                host=self.config["host"],
                user=self.config["user"],
                password=self.config["password"],
                database=self.config["database"]
            )
            return True  # Conexión exitosa
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)
            return False
        except UnicodeDecodeError as e:
            print("Contraseña o usuario no válidos, por favor vuelva a intentarlo")
            return False
        except Exception as e:
            print("Ocurrió un error inesperado al conectar:", e)
            return False


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
