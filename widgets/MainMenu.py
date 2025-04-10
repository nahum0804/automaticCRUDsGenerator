from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                            QFrame, QSizePolicy)
from PyQt5.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self, tablas_seleccionadas):
        print("Iniciando MainMenu")
        super().__init__()
        self.tablas_seleccionadas = tablas_seleccionadas  
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Título principal
        title = QLabel("Bienvenido al Menú Principal")
        title.setStyleSheet("font-size: 24px; color: #FFFFFF; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        
        # Subtítulo con las tablas seleccionadas
        subtitulo_texto = f"Tablas seleccionadas: {', '.join(self.tablas_seleccionadas)}"
        print("En Main menú")
        subtitulo = QLabel(subtitulo_texto)
        subtitulo.setStyleSheet("font-size: 16px; color: #4CAF50;")
        subtitulo.setAlignment(Qt.AlignCenter)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("color: #333333;")
        
        # Contenedor para los botones
        button_container = QWidget()
        button_layout = QVBoxLayout()
        button_layout.setSpacing(15)
        button_layout.setAlignment(Qt.AlignCenter)
        
        # Botón CRUD
        crud = QPushButton("Menú CRUD")
        crud.setStyleSheet("""
            QPushButton {
                background-color: #1E88E5;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                min-width: 300px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #42A5F5;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)
        crud.setCursor(Qt.PointingHandCursor)
        
        # Nuevo botón: Modo de Generación de Código
        code_gen = QPushButton("Modo de Generación de Código")
        code_gen.setStyleSheet("""
            QPushButton {
                background-color: #673AB7;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                min-width: 300px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #7E57C2;
            }
            QPushButton:pressed {
                background-color: #4527A0;
            }
        """)
        code_gen.setCursor(Qt.PointingHandCursor)
        
        # Nuevo botón: Generador de Procedimientos Almacenados
        sp_gen = QPushButton("Generador de Procedimientos Almacenados")
        sp_gen.setStyleSheet("""
            QPushButton {
                background-color: #009688;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 16px;
                min-width: 300px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #26A69A;
            }
            QPushButton:pressed {
                background-color: #00796B;
            }
        """)
        sp_gen.setCursor(Qt.PointingHandCursor)
        
        # Agregar botones al layout de botones
        button_layout.addWidget(crud)
        button_layout.addWidget(code_gen)
        button_layout.addWidget(sp_gen)
        button_container.setLayout(button_layout)
        
        # Agregar widgets al layout principal
        layout.addWidget(title)
        layout.addWidget(subtitulo)
        layout.addWidget(separator)
        layout.addWidget(button_container)
        layout.addStretch()
        
        self.setLayout(layout)