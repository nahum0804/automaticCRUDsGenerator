from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QFrame, QPushButton, QLabel)
from PyQt5.QtCore import Qt
from widgets.MainMenu import MainMenu

class TableWidget(QMainWindow):
    def __init__(self, tablas, parent=None):
        super().__init__(parent)
        self.tablas_seleccionadas = []
        self.tablas = tablas
        self.current_widget = None
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
            QPushButton:checked {
                background-color: #1B5E20;
            }
            QPushButtonConfirm {
                background-color: #20aeff;
                border: none;
                border-radius: 8px;
                padding: 14px;
                color: #FFFFFF;
                font-size: 16px;
                font-weight: bold;
                transition: all 0.3s;             
            }
            QPushButton#confirm_button {
                background-color: #2196F3;
                color: #FFFFFF;
            }
            QPushButton#confirm_button:hover {
                background-color: #1111F3;
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
        form_layout.addWidget(self.title)

        # Agregar un botón por cada tabla
        self.buttons = []
        for tabla in self.tablas:
            boton = QPushButton(tabla)
            boton.setCheckable(True)  # Para permitir selección múltiple
            boton.setFixedHeight(50)
            boton.clicked.connect(self.update_selection)
            form_layout.addWidget(boton)
            self.buttons.append(boton)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.setFixedHeight(50)
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.on_confirm)
        form_layout.addWidget(self.confirm_button)

        form_container.setLayout(form_layout)

        # Layout central
        central_layout = QHBoxLayout()
        central_layout.addStretch()
        central_layout.addWidget(form_container)
        central_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(central_layout)
        main_layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def update_selection(self):
        """Actualiza la lista de tablas seleccionadas cuando se hace clic en un botón"""
        self.tablas_seleccionadas = []
        for btn in self.buttons:
            if btn.isChecked():
                self.tablas_seleccionadas.append(btn.text())
        
        # Habilitar el botón de confirmar si hay al menos una tabla seleccionada
        self.confirm_button.setEnabled(len(self.tablas_seleccionadas) > 0)

    def on_confirm(self):
        if not self.tablas_seleccionadas:
            return
            
        print(f"Tablas seleccionadas: {', '.join(self.tablas_seleccionadas)}")
            
        # Pasar las tablas seleccionadas al MainMenu
        self.main_menu = MainMenu(self.tablas_seleccionadas, self)
        self.setCentralWidget(self.main_menu)
        self.current_widget = self.main_menu