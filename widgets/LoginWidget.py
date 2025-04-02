from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
                            QPushButton, QFrame)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_animations()
        
    def setup_ui(self):
        self.setWindowTitle("Acceso Futurista")
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
            QLineEdit {
                background-color: #252525;
                border: 2px solid transparent;
                border-radius: 8px;
                padding: 14px;
                color: #E0E0E0;
                font-size: 16px;
                transition: all 0.3s;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
                background-color: #2E2E2E;
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

        
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        form_container = QFrame()
        form_layout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignCenter)
        form_layout.setSpacing(20)

        self.title = QLabel("INICIO DE SESIÓN")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #4CAF50;")

        self.ip_input = self.create_input_field("Dirección IP:")
        self.user_input = self.create_input_field("Usuario:")
        self.pass_input = self.create_input_field("Contraseña:", is_password=True)

        self.login_btn = QPushButton("CONECTAR")
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.setFixedHeight(50)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #BDBDBD; font-size: 14px;")

        form_layout.addWidget(self.title)
        form_layout.addWidget(separator)
        form_layout.addSpacing(20) 

        form_layout.addWidget(self.ip_input["label"])
        form_layout.addWidget(self.ip_input["field"])
        form_layout.addSpacing(5)
        form_layout.addWidget(self.user_input["label"])
        form_layout.addWidget(self.user_input["field"])
        form_layout.addSpacing(5)
        form_layout.addWidget(self.pass_input["label"])
        form_layout.addWidget(self.pass_input["field"])

        form_layout.addSpacing(20)  
        form_layout.addWidget(self.login_btn)
        form_layout.addSpacing(10)
        form_layout.addWidget(self.status_label)

        form_container.setLayout(form_layout)


        central_layout = QHBoxLayout()
        central_layout.addStretch()
        central_layout.addWidget(form_container)
        central_layout.addStretch()

        main_layout.addStretch()
        main_layout.addLayout(central_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_input_field(self, label_text, is_password=False):
        label = QLabel(label_text)
        label.setStyleSheet("font-size: 18px; color: #BDBDBD; font-weight: bold;")

        field = QLineEdit()
        field.setFixedHeight(50)
        if is_password:
            field.setEchoMode(QLineEdit.Password)

        return {"label": label, "field": field}

    def setup_animations(self):
        self.btn_animation = QPropertyAnimation(self.login_btn, b"geometry")
        self.btn_animation.setDuration(100)
        self.btn_animation.setEasingCurve(QEasingCurve.OutQuad)
        
        self.login_btn.clicked.connect(self.animate_button)

    def animate_button(self):
        original_geometry = self.login_btn.geometry()
        self.btn_animation.setStartValue(original_geometry)
        self.btn_animation.setEndValue(original_geometry.adjusted(0, 2, 0, 2))
        self.btn_animation.start()
        
        self.btn_animation.finished.connect(
            lambda: self.btn_animation.setEndValue(original_geometry))

    def get_credentials(self):
        return {
            "ip": self.ip_input["field"].text(),
            "user": self.user_input["field"].text(),
            "password": self.pass_input["field"].text()
        }

    def set_status(self, message, is_error=False):
        color = "#FF5252" if is_error else "#4CAF50"
        self.status_label.setStyleSheet(f"color: {color}; font-size: 14px;")
        self.status_label.setText(message)
