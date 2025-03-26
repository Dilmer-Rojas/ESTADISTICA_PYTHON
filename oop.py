import numpy as np
import time
import os

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

class InterfazConsola:
    @staticmethod
    def obtener_lista():
        entrada = input("Ingrese los elementos de la lista separados por comas: ")
        return list(map(int, entrada.split(',')))
    
    @staticmethod
    def mostrar_menu():
        print("""
                MENÚ
        1. Media
        2. Mediana
        3. Moda
        4. Percentiles
        5. IQR
        6. Desviación Estándar
        7. Outliers (Desviación Estándar)
        8. Outliers (IQR)
        9. Salir
        """)
    
    @staticmethod
    def ejecutar():
        while True:
            InterfazConsola.mostrar_menu()
            opcion = input("Elija una opción: ")
            if opcion == '9':
                print("Saliendo...")
                time.sleep(2)
                break
            lista = InterfazConsola.obtener_lista()
            stats = Estadisticas(lista)
            if opcion == '1':
                print(f"Media: {stats.media()}")
            elif opcion == '2':
                print(f"Mediana: {stats.mediana()}")
            elif opcion == '3':
                print(f"Moda: {', '.join(map(str, stats.moda()))}")
            elif opcion == '4':
                percentiles = stats.percentiles()
                print(f"Percentiles -> P25: {percentiles[25]}, P50: {percentiles[50]}, P75: {percentiles[75]}")
            elif opcion == '5':
                print(f"IQR: {stats.iqr()}")
            elif opcion == '6':
                print(f"Desviación Estándar: {stats.desviacion_estandar()}")
            elif opcion == '7':
                outliers = stats.outliers_desviacion()
                print(f"Outliers (Desviación Estándar): {', '.join(map(str, outliers)) if outliers else 'Ninguno'}")
            elif opcion == '8':
                outliers = stats.outliers_iqr()
                print(f"Outliers (IQR): {', '.join(map(str, outliers)) if outliers else 'Ninguno'}")
            else:
                print("Opción inválida.")
            input("Presione Enter para continuar...")
            os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    InterfazConsola.ejecutar()
