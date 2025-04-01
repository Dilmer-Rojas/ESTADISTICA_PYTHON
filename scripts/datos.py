from tkinter import filedialog
from scipy import stats
import tkinter as tk
import pandas as pd
import sqlite3

# Menú de operaciones estadísticas
def menu_op():
    print("""
                MENÚ DE ANÁLISIS ESTADÍSTICO
        [1] Media
        [2] Mediana
        [3] Moda
        [4] Percentiles
        [5] Desviación Estándar
        [6] IQR (Rango intercuartil)
        [7] Outliers con std
        [8] Outliers con IQR
        [9] Salir
          """)

# Función para seleccionar un archivo
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", 
                                         filetypes=[("Archivos CSV", "*.csv"),
                                                    ("Archivos Excel", "*.xlsx"),
                                                    ("Bases de datos SQLite", "*.db"),
                                                    ("Todos los archivos", "*.*")])
    if archivo:
        print(f"\n📂 Archivo seleccionado: {archivo}")
        return archivo  
    else:
        print("⚠ No se seleccionó ningún archivo.")
        return None

# Función para obtener nombres de columnas automáticamente
def obtener_columnas(data, archivo=None, tabla=None):
    if isinstance(data, pd.DataFrame):
        columnas = data.columns.tolist()
    elif archivo and tabla:
        try:
            conn = sqlite3.connect(archivo)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({tabla});")
            columnas = [col[1] for col in cursor.fetchall()]
            conn.close()
        except sqlite3.Error as e:
            print(f"❌ Error al obtener columnas de la base de datos: {e}")
            return None
    else:
        print("⚠ No se pudo determinar las columnas.")
        return None

    print("\n📋 Columnas del dataset:")
    for col in columnas:
        print(f" - {col}")

    return columnas

# Función para mostrar las tablas de una base de datos SQLite
def mostrar_tablas_sqlite(archivo):
    try:
        conn = sqlite3.connect(archivo)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [tabla[0] for tabla in cursor.fetchall()]
        conn.close()
        
        if tablas:
            print("\n📌 Tablas en la base de datos:")
            for tabla in tablas:
                print(f"  - {tabla}")
        else:
            print("⚠ No hay tablas en la base de datos.")
    
    except sqlite3.Error as e:
        print(f"❌ Error al acceder a la base de datos: {e}")

# Seleccionando columna para el análisis
def seleccionar_columna(data):
    """
    Permite al usuario elegir una columna para análisis estadístico.
    """
    columnas = data.columns.tolist()
    print("\n📋 Columnas disponibles para análisis:")
    for i, col in enumerate(columnas, 1):
        print(f" [{i}] {col}")

    while True:
        try:
            indice = int(input("\nIngrese el número de la columna que desea analizar: ")) - 1
            if 0 <= indice < len(columnas):
                return columnas[indice]
            else:
                print("⚠ Número fuera de rango. Intente nuevamente.")
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")


# Función para manejar las opciones del menú
def menu_principal(data, archivo, tipo, nombre_tabla=None):
    columnas = obtener_columnas(data, archivo, nombre_tabla)

    while True:
        print("\n📊 Opciones:")
        print("[1] Mostrar dataset")
        print("[2] Acceder a operaciones estadísticas")
        print("[3] Salir")
        
        try:
            op = int(input("Elija una opción: "))
            
            if op == 1:
                print("\n🗂 Dataset:")
                print(data)
            elif op == 2:
                # menu_op()
                columna = seleccionar_columna(data)
                print(f"\n 📊 Análisis sobre la columna: {columna}")
                menu_op()
                opc = int(input("Elija una opción de análisis: "))
                if opc == 1:
                    print("\n📊 Media:")
                    print(data[columna].mean())
                elif opc == 2:
                    print("\n📊 Mediana:")
                    print(data[columna].median())
                elif opc == 3:
                    print("\n📊 Moda:")
                    print(data[columna].mode())
                elif opc == 4:
                    print("\n 📊 Percentiles:")
                    percentil = float(input("Ingrese el percentil (0-100): "))
                    print(data[columna].quantile(percentil / 100))
                else:
                    print("⚠ Opción no implementada.")
            elif op == 3:
                print("\n👋 Saliendo... ¡Gracias!")
                break
            else:
                print("⚠ Opción no válida. Intente nuevamente.")
        except ValueError:
            print("⚠ Debe ingresar un número válido.")

# Función principal
def main():
    input("\n🔎 Debe seleccionar un archivo (.csv, .xlsx, .db). Presione Enter para continuar...")
    archivo = seleccionar_archivo()

    if not archivo:
        print("⚠ No se seleccionó un archivo. Saliendo...")
        return
    
    extension = archivo.split(".")[-1]
    print(f"📝 Extensión del archivo: .{extension}")

    data = None
    nombre_tabla = None

    if extension == "csv":
        data = pd.read_csv(archivo)
    elif extension == "xlsx":
        data = pd.read_excel(archivo)
    elif extension == "db":
        mostrar_tablas_sqlite(archivo)
        nombre_tabla = input("\nIngrese el nombre de la tabla: ")
        try:
            conn = sqlite3.connect(archivo)
            query = f"SELECT * FROM {nombre_tabla};"
            data = pd.read_sql_query(query, conn)
            conn.close()
        except sqlite3.Error as e:
            print(f"❌ Error al acceder a la base de datos: {e}")
            return
    else:
        print(f"⚠ Extensión no compatible: .{extension}")
        return

    menu_principal(data, archivo, extension, nombre_tabla)

# Ejecutar el programa
if __name__ == "__main__":
    main()
