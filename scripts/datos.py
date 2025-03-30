from tkinter import filedialog
from scipy import stats
import tkinter as tk
import pandas as pd
import numpy as np
import sqlite3
import time
import os

# Menú de operaciones
def menu_op():
    print("""
                MENÚ
        [1] Media
        [2] Mediana
        [3] Moda
        [4] Desviación Estándar
        [5] Percentiles
        [6] IQR (Rango intercuartil)
        [7] Outliers con std
        [8] Outliers con IQR
        [9] Salir
          """)

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", 
                                         filetypes=[("Archivos CSV", "*.csv"),
                                                    ("Archivos Excel", "*.xlsx"),
                                                    ("Bases de datos SQLite", "*.db"),
                                                    ("Todos los archivos", "*.*")])
    
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
        return archivo  # Retorna la ruta del archivo
    else:
        print("No se seleccionó ningún archivo.")
        return None

def main():
    input("Debe seleccionar el archivo .csv, .xlsx, .db. Presione Enter para continuar...")
    time.sleep(2)  # Pausa antes de abrir el diálogo
    archivo = seleccionar_archivo()  # Obtiene la ruta del archivo

    if archivo:
        extension = archivo.split(".")[-1]  # Obtiene la extensión del archivo
        print(f"Extensión del archivo: .{extension}")
    else:
        print("No se pudo determinar la extensión porque no se seleccionó un archivo.")
    
    if extension == "csv":
        data = pd.read_csv(archivo)
        print("Ingrese 1 para mostrar el dataset...")
        print("Ingrese 2 si quiere acceder a las operaciones estadísticas...")
        print("Ingrese 3 para salir")
        op = int(input("Elija: "))
        if op == 1:
            print(data)
        elif op == 2:
            menu_op()
            opc = int(input("Elija una opción : "))
            if opc == 1:
                print("Media")
        else:
            print("Saliendo")
            time.sleep(2)
            print("Gracias!")
            exit
    elif extension == "xlsx":
        data = pd.read_excel(archivo)
        print("Ingrese 1 para mostrar el dataset...")
        print("Ingrese 2 si quiere acceder a las operaciones estadísticas...")
        print("Ingrese 3 para salir")
        op = int(input("Elija: "))
        if op == 1:
            print(data)
        elif op == 2:
            menu_op()
        else:
            print("Saliendo")
            time.sleep(2)
            print("Gracias!")
            exit
    elif extension == "db":
        try:
            # Conectar a la base de datos
            conn = sqlite3.connect(archivo)
            cursor = conn.cursor()

            # Obtener los nombres de las tablas
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tablas = cursor.fetchall()

            # Mostrar las tablas
            if tablas:
                print("Tablas en la base de datos:")
                for tabla in tablas:
                    print(f"- {tabla[0]}")
            else:
                print("No hay tablas en la base de datos.")

            
            print("Ingrese 1 para mostrar el dataset...")
            print("Ingrese 2 si quiere acceder a las operaciones estadísticas...")
            print("Ingrese 3 para salir")
            op = int(input("Elija: "))
            if op == 1:
                nombre_tabla = input("Ingrese el nombre de la tabla: ")
                query = f"SELECT * FROM {nombre_tabla};"
                query = pd.read_sql_query(query, conn)
                print(query)
            elif op == 2:
                menu_op()
            else:
                print("Saliendo")
                time.sleep(2)
                print("Gracias!")
                exit
            
            # Cerrar conexión
            conn.close()
        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
        
    else:
        print(f"Extensión del archivo no compatible: {extension}")
        print("Ingrese un archivo con estensión válida...")
        time.sleep(2)
        main()
# Llamada a la función principal
main()
