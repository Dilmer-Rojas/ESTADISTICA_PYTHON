import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class Estadisticas:
    def __init__(self, lista):
        self.lista = sorted(lista)
        self.n = len(lista)
    
    def media(self):
        return sum(self.lista) / self.n
    
    def mediana(self):
        if self.n % 2 == 1:
            return self.lista[self.n // 2]
        else:
            return (self.lista[self.n // 2 - 1] + self.lista[self.n // 2]) / 2
    
    def moda(self):
        repeticiones = {}
        for i in self.lista:
            repeticiones[i] = repeticiones.get(i, 0) + 1
        max_rep = max(repeticiones.values())
        return [k for k, v in repeticiones.items() if v == max_rep]
    
    def percentiles(self):
        arr = np.array(self.lista)
        return {25: np.percentile(arr, 25), 50: np.percentile(arr, 50), 75: np.percentile(arr, 75)}
    
    def iqr(self):
        Q1, Q3 = self.percentiles()[25], self.percentiles()[75]
        return Q3 - Q1
    
    def desviacion_estandar(self):
        return np.std(np.array(self.lista), ddof=1)
    
    def outliers_desviacion(self):
        media = np.mean(self.lista)
        desv_std = self.desviacion_estandar()
        lim_inf, lim_sup = media - (3 * desv_std), media + (3 * desv_std)
        return [x for x in self.lista if x < lim_inf or x > lim_sup]
    
    def outliers_iqr(self):
        Q1, Q3 = self.percentiles()[25], self.percentiles()[75]
        IQR = Q3 - Q1
        lim_inf, lim_sup = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        return [x for x in self.lista if x < lim_inf or x > lim_sup]

class EstadisticasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Calculadora Estadística")
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Ingrese los números separados por comas:")
        self.layout.addWidget(self.label)
        
        self.input = QLineEdit()
        self.layout.addWidget(self.input)
        
        self.buttons = {
            "Media": self.calcular_media,
            "Mediana": self.calcular_mediana,
            "Moda": self.calcular_moda,
            "Percentiles": self.calcular_percentiles,
            "IQR": self.calcular_iqr,
            "Desviación Estándar": self.calcular_desviacion,
            "Outliers (Desviación Estándar)": self.calcular_outliers_ds,
            "Outliers (IQR)": self.calcular_outliers_iqr,
        }
        
        for text, func in self.buttons.items():
            btn = QPushButton(text)
            btn.clicked.connect(func)
            self.layout.addWidget(btn)
        
        self.setLayout(self.layout)
    
    def obtener_lista(self):
        try:
            lista = list(map(int, self.input.text().split(',')))
            return Estadisticas(lista)
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese solo números separados por comas.")
            return None
    
    def calcular_media(self):
        stats = self.obtener_lista()
        if stats:
            QMessageBox.information(self, "Resultado", f"Media: {stats.media()}")
    
    def calcular_mediana(self):
        stats = self.obtener_lista()
        if stats:
            QMessageBox.information(self, "Resultado", f"Mediana: {stats.mediana()}")
    
    def calcular_moda(self):
        stats = self.obtener_lista()
        if stats:
            QMessageBox.information(self, "Resultado", f"Moda: {', '.join(map(str, stats.moda()))}")
    
    def calcular_percentiles(self):
        stats = self.obtener_lista()
        if stats:
            p = stats.percentiles()
            QMessageBox.information(self, "Resultado", f"P25: {p[25]}, P50: {p[50]}, P75: {p[75]}")
    
    def calcular_iqr(self):
        stats = self.obtener_lista()
        if stats:
            QMessageBox.information(self, "Resultado", f"IQR: {stats.iqr()}")
    
    def calcular_desviacion(self):
        stats = self.obtener_lista()
        if stats:
            QMessageBox.information(self, "Resultado", f"Desviación Estándar: {stats.desviacion_estandar()}")
    
    def calcular_outliers_ds(self):
        stats = self.obtener_lista()
        if stats:
            outliers = stats.outliers_desviacion()
            QMessageBox.information(self, "Resultado", f"Outliers (Desviación Estándar): {', '.join(map(str, outliers)) if outliers else 'Ninguno'}")
    
    def calcular_outliers_iqr(self):
        stats = self.obtener_lista()
        if stats:
            outliers = stats.outliers_iqr()
            QMessageBox.information(self, "Resultado", f"Outliers (IQR): {', '.join(map(str, outliers)) if outliers else 'Ninguno'}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EstadisticasApp()
    ventana.show()
    sys.exit(app.exec())
