from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout,
    QComboBox, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QFont

class SPGenerator(QWidget):
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
            QComboBox {
                background-color: #1f1f1f;
                border: 1px solid #2a2a2a;
                padding: 5px;
                border-radius: 10px;
                color: #ffffff;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Generador de Procedimientos Almacenados", self)
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        layout.addWidget(title)

        # Opciones de configuración
        config_layout = QHBoxLayout()
        self.combo_schema = QComboBox()
        self.combo_schema.addItems(["public", "admin", "otro_esquema"])  # Se puede hacer dinámico
        config_layout.addWidget(QLabel("Esquema:"))
        config_layout.addWidget(self.combo_schema)

        self.combo_modo = QComboBox()
        self.combo_modo.addItems(["Mostrar código", "Mostrar y ejecutar"])
        config_layout.addWidget(QLabel("Modo:"))
        config_layout.addWidget(self.combo_modo)

        self.prefijo_input = QComboBox()
        self.prefijo_input.setEditable(True)
        self.prefijo_input.setEditText("sp_")
        config_layout.addWidget(QLabel("Prefijo:"))
        config_layout.addWidget(self.prefijo_input)

        layout.addLayout(config_layout)

        # Caja de código generado
        self.code_box = QTextEdit()
        self.code_box.setPlaceholderText("Aquí se generará el procedimiento almacenado...")
        layout.addWidget(self.code_box)

        # Botones
        buttons_layout = QHBoxLayout()

        self.btn_generar = QPushButton("Generar SP")
        self.btn_generar.clicked.connect(self.generar_codigo)
        buttons_layout.addWidget(self.btn_generar)

        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_ejecutar.clicked.connect(self.ejecutar_codigo)
        buttons_layout.addWidget(self.btn_ejecutar)

        self.btn_copiar = QPushButton("Copiar código")
        self.btn_copiar.clicked.connect(self.copiar_codigo)
        buttons_layout.addWidget(self.btn_copiar)

        self.btn_volver = QPushButton("Volver")
        self.btn_volver.clicked.connect(self.volver_al_menu)
        buttons_layout.addWidget(self.btn_volver)

        layout.addLayout(buttons_layout)

    def generar_codigo(self):
        esquema = self.combo_schema.currentText()
        modo = self.combo_modo.currentText()
        prefijo = self.prefijo_input.currentText()

        codigo = "-- Generador de SP\n"
        for tabla in self.tablas_seleccionadas:
            codigo += f"CREATE OR REPLACE PROCEDURE {esquema}.{prefijo}{tabla}_insert() \nAS $$\nBEGIN\n    -- Lógica para {tabla}\nEND;\n$$ LANGUAGE plpgsql;\n\n"

        self.code_box.setPlainText(codigo)

    def ejecutar_codigo(self):
        sql = self.code_box.toPlainText()
        if not sql.strip():
            return

        try:
            from db.dbConnector import PostgresDB
            db = PostgresDB("localhost", "admin", "admin123", "Tienda")
            if db.conectar():
                db.ejecutar_consulta(sql)
                self.code_box.append("\n--Procedimientos ejecutados correctamente")
                db.cerrar_conexion()
        except Exception as e:
            self.code_box.append(f"\n-- Error al ejecutar: {str(e)}")

    def copiar_codigo(self):
        QGuiApplication.clipboard().setText(self.code_box.toPlainText())

    def volver_al_menu(self):
        from widgets.MainMenu import MainMenu
        self.parent_window.setCentralWidget(MainMenu(self.tablas_seleccionadas, self.parent_window))
