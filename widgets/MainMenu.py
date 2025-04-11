from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                            QFrame, QSizePolicy)
from PyQt5.QtCore import Qt

from widgets.CodeGenerator import CodeGenerator
from widgets.SPGenerator import SPGenerator
# from widgets.CRUDMenu import CRUDMenu  # Descomenta cuando implementes CRUDMenu

class MainMenu(QWidget):
    def __init__(self, tablas_seleccionadas, parent=None):
        print("Iniciando MainMenu")
        super().__init__(parent)
        self.tablas_seleccionadas = tablas_seleccionadas
        self.parent_window = parent  
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
        btn_crud = QPushButton("Menú CRUD")
        btn_crud.setStyleSheet("""
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
        #btn_crud.setCursor(Qt.PointingHandCursor)
        #btn_crud.clicked.connect(self.open_crud_menu)
        
        # Botón: Modo de Generación de Código
        btn_code_gen = QPushButton("Modo de Generación de Código")
        btn_code_gen.setStyleSheet("""
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
        btn_code_gen.setCursor(Qt.PointingHandCursor)
        btn_code_gen.clicked.connect(self.open_code_generator)
        
        # Botón: Generador de Procedimientos Almacenados
        btn_sp_gen = QPushButton("Generador de Procedimientos Almacenados")
        btn_sp_gen.setStyleSheet("""
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
        btn_sp_gen.setCursor(Qt.PointingHandCursor)
        btn_sp_gen.clicked.connect(self.open_sp_generator)
        
        # Agregar botones al layout de botones
        button_layout.addWidget(btn_crud)
        button_layout.addWidget(btn_code_gen)
        button_layout.addWidget(btn_sp_gen)
        button_container.setLayout(button_layout)
        
        # Agregar widgets al layout principal
        layout.addWidget(title)
        layout.addWidget(subtitulo)
        layout.addWidget(separator)
        layout.addWidget(button_container)
        layout.addStretch()
        
        self.setLayout(layout)

    def open_code_generator(self):
        print("Entra a open_code_generator")
        if self.parent_window:
            self.parent_window.setCentralWidget(CodeGenerator(self.tablas_seleccionadas,self.parent_window))

    '''def open_crud_menu(self):
        """Abre el menú CRUD"""
        if self.parent_window:
            print("Abriendo CRUDMenu (implementar esta clase)")
            # self.crud_menu = CRUDMenu(self.tablas_seleccionadas, self.parent_window)
            # self.parent_window.setCentralWidget(self.crud_menu)
    '''
            


    def open_sp_generator(self):
        if self.parent_window:
            print("Entra a open_sp_generator")
            self.parent_window.setCentralWidget(SPGenerator(self.tablas_seleccionadas, self.parent_window))
            print( f"Tablas seleccionadas: {', '.join(self.tablas_seleccionadas)}")