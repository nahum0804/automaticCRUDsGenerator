from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QMainWindow)
from PyQt5.QtCore import Qt
from .MainMenu import MainMenu

class TableWidget(QMainWindow):  # Cambié QWidget por QMainWindow
    def __init__(self, tablas, parent=None):
        super().__init__(parent)
        self.tablas = tablas
        self.current_widget = None  # Inicializar el widget actual
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Tablas Disponibles")
        self.setGeometry(0, 0, 1200, 800)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
            }
            QFrame {
                background-color: #1E1E1E;
                border-radius: 12px;
                padding: 15px;
                box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                border-radius: 8px;
                padding: 14px;
                color: #FFFFFF;
                font-size: 16px;
                font-weight: bold;
                transition: all 0.3s;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
            QPushButton:pressed {
                background-color: #1B5E20;
            }
        """)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Contenedor del formulario
        form_container = QFrame()
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)
        form_layout.setSpacing(20)

        # Título
        self.title = QLabel("Tablas Disponibles")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")

        # Agregar el título
        form_layout.addWidget(self.title)

        # Agregar un botón por cada tabla
        for tabla in self.tablas:
            boton = QPushButton(tabla)
            boton.setFixedHeight(50)
            boton.clicked.connect(lambda checked, t=tabla: self.on_table_selected(t))
            form_layout.addWidget(boton)

        form_container.setLayout(form_layout)

        # Layout central
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        central_layout.addWidget(form_container)
        central_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(central_layout)
        main_layout.addStretch()

        # Establecer el layout en el widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)  # Esto ahora funciona

    def on_table_selected(self, tabla):
        print(f"Se seleccionó la tabla: {tabla}")
        
        # Si ya hay un widget actual, lo eliminamos
        if self.current_widget:
            self.current_widget.deleteLater()

        # Crear y mostrar el nuevo MainMenu
        self.main_menu = MainMenu()
        self.setCentralWidget(self.main_menu)  # Establecer el nuevo widget
        self.current_widget = self.main_menu  # Actualizar current_widget
