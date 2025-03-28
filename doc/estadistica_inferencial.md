# **Módulo 3: Estadística Inferencial**

📌 **Objetivo:** Comprender los fundamentos de la estadística inferencial y su aplicación en el análisis de datos mediante Python.

---

## **1. Introducción a la Estadística Inferencial**
La estadística inferencial permite hacer conclusiones sobre una población a partir de una muestra. Se basa en la teoría de probabilidades para estimar parámetros y realizar pruebas de hipótesis.

🔹 **Diferencia con la estadística descriptiva:** Mientras que la estadística descriptiva resume los datos, la inferencial permite extrapolar resultados y tomar decisiones basadas en evidencias.

Principales herramientas:
- Estimación de parámetros
- Intervalos de confianza
- Pruebas de hipótesis

---

## **2. Estimación de Parámetros**
La estimación es el proceso de inferir el valor de un parámetro poblacional a partir de una muestra. Se divide en:

🔹 **Estimación puntual:** Un único valor como mejor aproximación al parámetro desconocido. Ejemplo: la media muestral (éx) como estimador de la media poblacional (μ).

🔹 **Estimación por intervalo:** Un rango de valores que probablemente contenga el parámetro poblacional, expresado mediante intervalos de confianza.

### **Ejemplo en Python:**
```python
import numpy as np
import scipy.stats as st

# Datos de una muestra
muestra = [12, 15, 14, 10, 18, 20, 11, 13, 17, 19]

# Estimación puntual (media muestral)
media_muestral = np.mean(muestra)
print(f"Media muestral: {media_muestral}")
```

📌 **Interpretación:** La media de la muestra se usa como mejor estimador de la media poblacional.

---

## **3. Intervalos de Confianza**
Un intervalo de confianza (IC) proporciona un rango en el que es probable que se encuentre el parámetro poblacional.

### **Fórmula del Intervalo de Confianza para la Media:**
\[
IC = \bar{X} \pm Z \left( \frac{\sigma}{\sqrt{n}} \right)
\]

Donde:
- \(\bar{X}\) es la media muestral.
- \(Z\) es el valor crítico de la distribución normal para el nivel de confianza deseado.
- \(\sigma\) es la desviación estándar.
- \(n\) es el tamaño de la muestra.

### **Ejemplo en Python:**
```python
confianza = 0.95
desviacion_muestral = np.std(muestra, ddof=1)
n = len(muestra)
error_estandar = desviacion_muestral / np.sqrt(n)

# Cálculo del intervalo de confianza
intervalo = st.t.interval(confianza, df=n-1, loc=media_muestral, scale=error_estandar)
print(f"Intervalo de confianza al 95%: {intervalo}")
```
📌 **Interpretación:** El verdadero valor de la media poblacional tiene un 95% de probabilidad de estar dentro de este rango.

---

## **4. Pruebas de Hipótesis**
Las pruebas de hipótesis permiten evaluar afirmaciones sobre una población utilizando datos muestrales.

🔹 **Hipótesis Nula (H₀):** No hay diferencia o efecto significativo.
🔹 **Hipótesis Alternativa (H₁):** Existe una diferencia o efecto significativo.

Pasos para realizar una prueba de hipótesis:
1. Plantear H₀ y H₁.
2. Elegir el nivel de significancia (generalmente 0.05).
3. Calcular el estadístico de prueba.
4. Comparar con el valor crítico o calcular el p-valor.
5. Tomar una decisión (rechazar o no H₀).

### **Ejemplo: Prueba t para una media poblacional**
```python
# Hipótesis: La media poblacional es 15
valor_hipotetico = 15

# Prueba t
t_stat, p_valor = st.ttest_1samp(muestra, valor_hipotetico)
print(f"Estadístico t: {t_stat}, p-valor: {p_valor}")

# Decisión basada en el p-valor
if p_valor < 0.05:
    print("Rechazamos la hipótesis nula (H₀): la media poblacional es diferente de 15.")
else:
    print("No hay suficiente evidencia para rechazar H₀.")
```
📌 **Interpretación:** Si el p-valor es menor a 0.05, se rechaza H₀, indicando que la media poblacional probablemente no sea 15.

---

## **5. Tipos de Errores en Pruebas de Hipótesis**
Cuando realizamos pruebas de hipótesis, podemos cometer errores:
- **Error Tipo I (α):** Rechazar H₀ cuando es verdadera (falso positivo).
- **Error Tipo II (β):** No rechazar H₀ cuando es falsa (falso negativo).

El nivel de significancia (α) define la probabilidad de cometer un error Tipo I. Valores comunes son 0.05 o 0.01.

---

## **Conclusiones**
La estadística inferencial nos permite extraer conclusiones sobre poblaciones a partir de muestras mediante estimaciones e inferencias.
- Los **intervalos de confianza** proporcionan rangos probables para parámetros desconocidos.
- Las **pruebas de hipótesis** ayudan a evaluar afirmaciones y tomar decisiones informadas.

