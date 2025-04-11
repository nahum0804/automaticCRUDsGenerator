from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QGuiApplication, QFont

class CodeGenerator(QWidget):
    def __init__(self, tablas_seleccionadas, parent=None):
        super().__init__(parent)
        self.tablas_seleccionadas = tablas_seleccionadas
        self.parent_window = parent
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #ffffff;
                font-family: 'Segoe UI';
            }
            QPushButton {
                background-color: #1f1f1f;
                border: 1px solid #2a2a2a;
                padding: 8px 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2e2e2e;
            }
            QTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #2c2c2c;
                border-radius: 10px;
                color: #ffffff;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Generador de Código SQL", self)
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        layout.addWidget(title)

        self.code_box = QTextEdit()
        self.code_box.setPlaceholderText("Aquí se generará el código...")
        layout.addWidget(self.code_box)

        buttons_layout = QHBoxLayout()

        self.btn_generar = QPushButton("Generar Código")
        self.btn_generar.clicked.connect(self.generar_codigo)
        buttons_layout.addWidget(self.btn_generar)

        self.btn_copiar = QPushButton("Copiar")
        self.btn_copiar.clicked.connect(self.copiar_codigo)
        buttons_layout.addWidget(self.btn_copiar)

        self.btn_volver = QPushButton("Volver")
        self.btn_volver.clicked.connect(self.volver_al_menu)
        buttons_layout.addWidget(self.btn_volver)

        layout.addLayout(buttons_layout)

    def generar_codigo(self):
        codigo = "-- Código generado dinámicamente:\n"
        for tabla in self.tablas_seleccionadas:
            codigo += f"SELECT * FROM {tabla};\n"
        self.code_box.setPlainText(codigo)

    def copiar_codigo(self):
        QGuiApplication.clipboard().setText(self.code_box.toPlainText())

    def volver_al_menu(self):
        from widgets.MainMenu import MainMenu
        self.parent_window.setCentralWidget(MainMenu(self.tablas_seleccionadas, self.parent_window))
