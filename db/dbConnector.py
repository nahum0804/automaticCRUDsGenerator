import psycopg2
import json
class PostgresDB:
    def __init__(self, user, password, dbname="usuariodb", port=5432):
        self.config = {
            "host": "127.0.0.1",  # <- Quita el .encode()
            "user": user,
            "password": password,
            "dbname": dbname,
            "port": port
        }
        self.conexion = None

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
        """Establece la conexión con la base de datos."""
        print("Conectando a PostgreSQL...")
        try:
            print("📦 Config recibida:", self.config)
            for k, v in self.config.items():
                print(f"{k}: {v} ({type(v)})")
            self.conexion = psycopg2.connect(**self.config)  # <- Sin clean_config
            print("✅ Conexión exitosa a PostgreSQL")
            return True
        except psycopg2.Error as e:
            print("❌ Error al conectar a PostgreSQL:", e)
            self.conexion = None
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
