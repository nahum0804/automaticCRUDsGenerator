import sys
from PyQt5.QtWidgets import QApplication
from widgets.MainWindow import MainWindow

def main():
    # Configuración de la aplicación
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Crear y mostrar ventana principal
    window = MainWindow()
    window.show()
    
    # Ejecutar bucle principal
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()