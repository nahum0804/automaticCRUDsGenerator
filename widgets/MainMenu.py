from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, 
                            QFrame, QSizePolicy)
from PyQt5.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        
        # Título
        title = QLabel("Bienvenido al Menú Principal")
        title.setStyleSheet("font-size: 24px; color: #FFFFFF;")
        title.setAlignment(Qt.AlignCenter)
        
        # Separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("color: #333333;")
        
        # Botón de ejemplo
        example_btn = QPushButton("Menú CRUD")
        example_btn.setStyleSheet("""
            QPushButton {
                background-color: #1E88E5;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #42A5F5;
            }
        """)
        example_btn.setCursor(Qt.PointingHandCursor)
        
        # Agregar elementos
        layout.addWidget(title)
        layout.addWidget(separator)
        layout.addWidget(example_btn)
        layout.addStretch()
        
        self.setLayout(layout)