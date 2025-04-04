from PyQt5.QtWidgets import QApplication, QMainWindow
from .LoginWidget import LoginWidget
from .MainMenu import MainMenu
import time

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
        
        print("Credenciales ingresadas:", credentials)
        self.login_widget.set_status("Conectando...")

        QApplication.processEvents()
        time.sleep(1)  
        
        self.show_main_menu()

    def show_login_screen(self):
        if self.current_widget:
            self.current_widget.deleteLater()  
        
        self.login_widget = LoginWidget()
        self.setCentralWidget(self.login_widget)
        self.current_widget = self.login_widget 
        
        self.login_widget.login_btn.clicked.connect(self.handle_login)

    def show_main_menu(self):
        if self.current_widget:
            self.current_widget.deleteLater() 

        self.main_menu = MainMenu()
        self.setCentralWidget(self.main_menu)
        self.current_widget = self.main_menu  
        print("Menú principal cargado correctamente.")