from PyQt5.QtWidgets import QApplication, QMainWindow
from .LoginWidget import LoginWidget
from .MainMenu import MainMenu
import time 
from db.dbConnector import PostgresDB   
from helpers import selectorTables
from widgets.TableWidget import TableWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CRUD Generator")
        self.setStyleSheet("background-color: #121212;")
        self.setGeometry(100, 100, 800, 600)
        
        self.current_widget = None

        self.show_login_screen()
    
    def handle_login(self):
        credentials = self.login_widget.get_credentials()
        
        if not all(credentials.values()):
            self.login_widget.set_status("Todos los campos son requeridos", is_error=True)
            return
        
        self.login_widget.set_status("Conectando...")
        QApplication.processEvents()

        # Crear instancia de PostgresDB con credenciales de administración
        db = PostgresDB(
            host= credentials["ip"],
            user=credentials["user"],   
            password=credentials["password"],
            database="Tienda"
        )

        # Intentar conectar
        if db.conectar():
            print("Conexión exitosa a PostgreSQL")
            # Verificar credenciales contra tabla usuarios
            # if db.verificar_usuario(credentials["user"], credentials["password"]):
            #    self.login_widget.set_status("¡Conexión exitosa!")
            #    self.db = db
            self.show_main_menu(credentials["user"], credentials["password"], credentials["ip"])
            #else:
            #    self.login_widget.set_status("Usuario o contraseña incorrectos", is_error=True)
            #    db.cerrar_conexion() 
        else:
            self.login_widget.set_status("Fallo al conectar a la base de datos", is_error=True)

    def show_login_screen(self):
        if self.current_widget:
            self.current_widget.deleteLater()  
        
        self.login_widget = LoginWidget()
        self.setCentralWidget(self.login_widget)
        self.current_widget = self.login_widget 
        
        self.login_widget.login_btn.clicked.connect(self.handle_login)

    def show_main_menu(self, user, password, ip):
        print("Menú principal cargado correctamente.")
        rol = selectorTables.autenticar_usuario(user, password,ip)
        Permisos = rol["permisos"]
        tablas = selectorTables.mostrar_tablas_disponibles(Permisos)
        if self.current_widget:
            self.current_widget.deleteLater() 
        self.main_table_widget = TableWidget(tablas)
        self.setCentralWidget(self.main_table_widget)
        self.current_widget = self.main_table_widget 
   