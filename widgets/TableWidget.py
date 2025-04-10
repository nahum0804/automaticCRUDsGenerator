from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel

class TableWidget(QWidget):
    def __init__(self, data, headers, table_name):
        super().__init__()

        self.setWindowTitle(f"Tabla: {table_name}")
        self.layout = QVBoxLayout()

        # Etiqueta con el nombre de la tabla
        self.title = QLabel(f"📋 Mostrando datos de: {table_name}")
        self.layout.addWidget(self.title)

        # Crear la tabla
        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        # Llenar la tabla con datos
        for row_idx, row_data in enumerate(data):
            for col_idx, item in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)