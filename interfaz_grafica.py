import sys
import pandas as pd
import sqlite3
import numpy as np
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, 
                             QFileDialog, QComboBox, QMessageBox, QDialog)

class EstadisticasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.df = None  # DataFrame donde se cargará el archivo

    def initUI(self):
        self.setWindowTitle("Calculadora Estadística")
        self.setGeometry(100, 100, 400, 250)
        layout = QVBoxLayout()
        
        self.label = QLabel("Seleccione un archivo CSV, Excel o base de datos:")
        layout.addWidget(self.label)
        
        self.btn_cargar = QPushButton("Cargar Archivo")
        self.btn_cargar.clicked.connect(self.cargar_archivo)
        layout.addWidget(self.btn_cargar)
        
        self.combo_tablas = QComboBox()
        self.combo_tablas.setEnabled(False)
        layout.addWidget(self.combo_tablas)
        
        self.combo_columnas = QComboBox()
        self.combo_columnas.setEnabled(False)
        layout.addWidget(self.combo_columnas)
        
        self.btn_ir = QPushButton("Ir")
        self.btn_ir.setEnabled(False)
        self.btn_ir.clicked.connect(self.mostrar_menu)
        layout.addWidget(self.btn_ir)
        
        self.setLayout(layout)
    
    def cargar_archivo(self):
        opciones = "Archivos (*.csv *.xlsx *.db)"
        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", opciones)
        
        if not ruta:
            return
        
        if ruta.endswith(".csv"):
            self.df = pd.read_csv(ruta)
        elif ruta.endswith(".xlsx"):
            self.df = pd.read_excel(ruta)
        elif ruta.endswith(".db"):
            self.con = sqlite3.connect(ruta)
            cursor = self.con.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tablas = [tabla[0] for tabla in cursor.fetchall()]
            self.combo_tablas.clear()
            self.combo_tablas.addItems(tablas)
            self.combo_tablas.setEnabled(True)
            self.combo_tablas.currentIndexChanged.connect(self.cargar_columnas)
            return
        
        if self.df is not None:
            self.combo_columnas.clear()
            self.combo_columnas.addItems(self.df.columns)
            self.combo_columnas.setEnabled(True)
            self.btn_ir.setEnabled(True)
    
    def cargar_columnas(self):
        tabla_seleccionada = self.combo_tablas.currentText()
        if not tabla_seleccionada:
            return
        
        cursor = self.con.cursor()
        cursor.execute(f"PRAGMA table_info({tabla_seleccionada})")
        columnas = [col[1] for col in cursor.fetchall()]
        
        self.combo_columnas.clear()
        self.combo_columnas.addItems(columnas)
        self.combo_columnas.setEnabled(True)
        self.btn_ir.setEnabled(True)
    
    def mostrar_menu(self):
        columna = self.combo_columnas.currentText()
        if not columna:
            QMessageBox.warning(self, "Error", "Debe seleccionar una columna")
            return
        
        if hasattr(self, 'con') and self.con:
            query = f"SELECT {columna} FROM {self.combo_tablas.currentText()}"
            self.df = pd.read_sql(query, self.con)
        
        menu_dialogo = MenuEstadisticas(self.df[columna].dropna())
        menu_dialogo.exec()

class MenuEstadisticas(QDialog):
    def __init__(self, serie):
        super().__init__()
        self.serie = serie.astype(float)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Menú de Estadísticas")
        self.setGeometry(150, 150, 300, 400)
        layout = QVBoxLayout()
        
        opciones = ["Media", "Mediana", "Moda", "Percentiles", "IQR", 
                    "Desviación Estándar", "Outliers (Desviación Estándar)", "Outliers (IQR)"]
        self.combo_opciones = QComboBox()
        self.combo_opciones.addItems(opciones)
        layout.addWidget(self.combo_opciones)
        
        self.btn_calcular = QPushButton("Calcular")
        self.btn_calcular.clicked.connect(self.calcular_estadistica)
        layout.addWidget(self.btn_calcular)
        
        self.label_resultado = QLabel("Resultado: ")
        layout.addWidget(self.label_resultado)
        
        self.setLayout(layout)
    
    def calcular_estadistica(self):
        opcion = self.combo_opciones.currentText()
        resultado = ""
        
        if opcion == "Media":
            resultado = self.serie.mean()
        elif opcion == "Mediana":
            resultado = self.serie.median()
        elif opcion == "Moda":
            resultado = self.serie.mode().values
        elif opcion == "Percentiles":
            resultado = np.percentile(self.serie, [25, 50, 75])
        elif opcion == "IQR":
            q1, q3 = np.percentile(self.serie, [25, 75])
            resultado = q3 - q1
        elif opcion == "Desviación Estándar":
            resultado = self.serie.std()
        elif opcion == "Outliers (Desviación Estándar)":
            media, std = self.serie.mean(), self.serie.std()
            outliers = self.serie[(self.serie < media - 3*std) | (self.serie > media + 3*std)]
            resultado = outliers.values
        elif opcion == "Outliers (IQR)":
            q1, q3 = np.percentile(self.serie, [25, 75])
            iqr = q3 - q1
            outliers = self.serie[(self.serie < q1 - 1.5*iqr) | (self.serie > q3 + 1.5*iqr)]
            resultado = outliers.values
        
        self.label_resultado.setText(f"Resultado: {resultado}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EstadisticasApp()
    ventana.show()
    sys.exit(app.exec())