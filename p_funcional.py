import numpy as np
import time
import os

# Promedio o media
def media(lista, n):
    suma = 0
    for i in lista:
        suma += i
    promedio = (suma) / n
    return promedio

# Mediana
def mediana(lista, n):
    if n % 2 == 1:
        return lista[n // 2]
    else:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2


# Moda
def moda(lista):
    repeticiones = {}
    for i in lista:
        if i in repeticiones:
            repeticiones[i] += 1
        else:
            repeticiones[i] = 1
    max_repeticiones = max(repeticiones.values())
    
    modas = [k for k, v in repeticiones.items() if v == max_repeticiones]
    return modas

# Percentiles
def percentiles(lista):
    arr = np.array(lista)
    p25 = np.percentile(arr, 25)
    p50 = np.percentile(arr, 50)
    p75 = np.percentile(arr, 75)
    print("Los percentiles son: \n")
    print(f" p25 : {p25}\n p50 : {p50}\n p75 : {p75}")


# Rango Intercuartil - IQR
def iqr(lista):
    arr = np.array(lista)
    Q1 = np.percentile(arr, 25)
    Q3 = np.percentile(arr, 75)
    IQR = Q3 - Q1
    return IQR

# Desviación Estándar
def ds(lista):
    arr = np.array(lista)
    desv_std = np.std(arr, ddof=1) # ddof=1 para datos muestrales en lugar de poblacionales
    return desv_std


# Valores atípicos con desviación estandar
def atp_ds(lista):
    arr = np.array(lista)
    media = np.mean(arr)
    desv_std = np.std(arr, ddof=1) # ddof=1 para datos muestrales en lugar de poblacionales
    # Definir umbrales para outliers (usamos 3 desviaciones estándar)
    limite_inferior = media - (3 * desv_std)
    limite_superior = media + (3 * desv_std)
    # Identificar outliers
    outliers = [x for x in arr if x < limite_inferior or x > limite_superior]
    cantidad_outliers = 0
    for i in outliers:
        cantidad_outliers += 1
    print(f" La media o promedio : {media}")
    print(f" La desviación estándar muestral : {desv_std}")
    print(f" El límite inferior : {limite_inferior}")
    print(f" El límite superior : {limite_superior}")
    print(f" La cantidad de outliers detectados: {cantidad_outliers}")
    print(f" Los Outliers detectados: {outliers}")


# Valores atípicos usando IQR
def out_iqr(lista):
    arr = np.array(lista)
    Q1 = np.percentile(arr, 25)
    Q3 = np.percentile(arr, 75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = arr[(arr < limite_inferior) | (arr > limite_superior)]
    cantidad_outliers = 0
    for i in outliers:
        cantidad_outliers += 1
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print(f"Límite inferior : {limite_inferior}")
    print(f"Límite superior : {limite_superior}")
    print(f"La cantidad de outliers: {cantidad_outliers}")
    print("Outliers detectados:", ", ".join(map(str, outliers)))  # Outliers separados por comas
    pass


# Función principal
def main():
    print("""
                MENÚ
        1. Calcular la media (promedio)
        2. Calcular la mediana
        3. Calcular la moda
        4. Calcular los percentiles
        5. Calcular el IQR(Rango Intercuartil)
        6. Calcular la desviación estandar
        7. Outliers con Desviación Estándar
        8. Outliers con Rango Intercuartil (IQR)
        9. Salir
          """)
    while True:
        opc = int(input("Elija una opción: "))
        if opc == 1:
            print("")
            print("[Calcular la media (promedio)]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            n = len(lista)
            resultado = media(lista, n)
            print(f"La media o promedio de {lista} es: {resultado}")
            pass
        elif opc == 2:
            print("")
            print("[Calcular la mediana]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            n = len(lista)
            resultado = mediana(lista, n)
            print(f"La mediana de {lista} es: {resultado}")
            pass
        elif opc == 3:
            print("")
            print("[Calcular la moda]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            resultado = moda(lista)
            print(f"La(s) moda(s) encontrada(s): {resultado}")
            pass
        elif opc == 4:
            print("")
            print("[Calcular los percentiles]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            n = len(lista)
            percentiles(lista)
            pass
        elif opc == 5:
            print("")
            print("[Calcular el IQR(Rango Intercuartil)]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            resultado = iqr(lista)
            print(f"El rango intercuartil (IQR) es : {resultado}")
        elif opc == 6:
            print("")
            print("[Desviacíon Estándar]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            resultado = ds(lista)
            print(f"La desviación estándar es : {resultado}")
        elif opc == 7:
            print("")
            print("[Outliers - Valores Atípicos - Desviación Estándar]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            atp_ds(lista)
        elif opc == 8:
            print("")
            print("[Outliers - Valores Atípicos - IQR]")
            print("")
            lista = input("Ingrese los elementos de la lista separados por comas, 1,2,3: ").split(",")
            lista = [int(i) for i in lista]
            #Ordenamos los elementos de la lista
            lista.sort()
            out_iqr(lista)
        elif opc == 9:
            os.system("cls")
            print("Muchas gracias")
            print("Saliendo...")
            time.sleep(2)
            exit()
        else:
            print("Opción Inválida")
            time.sleep(1)
            os.system("cls") # Investigar para que funcione para windows, linux, etc
            main()
main()
