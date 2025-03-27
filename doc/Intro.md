¡Entendido! Aquí tienes el **Módulo 1: Fundamentos de Estadística Descriptiva**, con teoría y código en Python.  

---

# **Módulo 1: Fundamentos de Estadística Descriptiva**  

📌 **Objetivo:** Aprender los conceptos básicos de estadística descriptiva y cómo calcularlos en Python.  

## **1. Introducción a la Estadística Descriptiva**  

La **estadística descriptiva** se encarga de resumir y analizar datos sin extraer conclusiones generales. Nos permite entender cómo se distribuyen los datos y encontrar patrones en ellos.  

### 🔹 **Conceptos clave**  
- **Población:** Conjunto total de elementos bajo estudio.  
- **Muestra:** Subconjunto de la población, seleccionado para el análisis.  
- **Variable:** Característica de interés en un estudio (puede ser numérica o categórica).  
- **Tipos de datos:**  
  - **Cuantitativos:** Números (ejemplo: edad, salario, temperatura).  
  - **Cualitativos:** Categorías o etiquetas (ejemplo: género, color, estado civil).  

---

## **2. Medidas de Tendencia Central**  

Las medidas de tendencia central indican el valor típico o representativo de un conjunto de datos.  

### 🔹 **Media (Promedio)**  
Es la suma de todos los valores dividida entre el número de observaciones.  

```python
import numpy as np

datos = [12, 15, 14, 10, 8, 9, 13, 17, 15, 11]
media = np.mean(datos)
print(f"La media es: {media}")
```

📌 **Interpretación:** Si la media de los salarios en una empresa es de **$1500**, significa que en promedio los empleados ganan esa cantidad.  

### 🔹 **Mediana**  
Es el valor central cuando los datos están ordenados.  

```python
mediana = np.median(datos)
print(f"La mediana es: {mediana}")
```

📌 **Interpretación:** Se usa cuando hay valores extremos que afectan la media, como los ingresos en un país.  

### 🔹 **Moda**  
Es el valor que más se repite en un conjunto de datos.  

```python
from scipy import stats

moda = stats.mode(datos, keepdims=True)
print(f"La moda es: {moda.mode[0]}")
```

📌 **Ejemplo:** En un grupo de 50 estudiantes, si la calificación más frecuente es **8**, entonces **8 es la moda**.  

# **Medidas de Dispersión**

📌 **Objetivo:** Comprender cómo las medidas de dispersión nos ayudan a evaluar la variabilidad de los datos en un conjunto y calcularlas en Python con ejemplos detallados.

---

## **1. Introducción a las Medidas de Dispersión**
Las medidas de dispersión describen cómo se distribuyen los datos en relación con la media. Son fundamentales en el análisis estadístico, ya que permiten entender la estabilidad y la homogeneidad de los datos.

Las principales medidas de dispersión son:
- **Rango**
- **Varianza**
- **Desviación estándar**
- **Coeficiente de variación**

Estas medidas nos indican si los datos están muy dispersos o concentrados cerca de la media.

---

## **2. Rango**
El rango es la diferencia entre el valor máximo y el mínimo de un conjunto de datos. Es la medida más simple de dispersión, pero puede ser engañosa si existen valores atípicos extremos.

### **Fórmula del Rango:**
\[ Rango = X_{máx} - X_{mín} \]

### **Ejemplo en Python:**
```python
import numpy as np

datos = [5, 10, 15, 20, 25]
rango = np.max(datos) - np.min(datos)
print(f"El rango es: {rango}")  # Salida: 20
```

📌 **Interpretación:** Un rango alto indica gran dispersión entre los valores más extremos.

---

## **3. Varianza**
La varianza mide la dispersión de los datos con respecto a la media. Se calcula como el promedio de los cuadrados de las diferencias entre cada dato y la media.

### **Fórmula de la Varianza Poblacional:**
\[ \sigma^2 = \frac{\sum (X_i - \mu)^2}{N} \]

### **Fórmula de la Varianza Muestral:**
\[ s^2 = \frac{\sum (X_i - \bar{X})^2}{n-1} \]

Donde:
- \(X_i\) son los valores individuales del conjunto de datos.
- \(\mu\) es la media poblacional.
- \(\bar{X}\) es la media muestral.
- \(N\) es el tamaño de la población.
- \(n\) es el tamaño de la muestra.

### **Ejemplo en Python:**
```python
datos = [10, 20, 30, 40, 50]
varianza_poblacional = np.var(datos)
varianza_muestral = np.var(datos, ddof=1)
print(f"Varianza poblacional: {varianza_poblacional}")
print(f"Varianza muestral: {varianza_muestral}")
```

📌 **Interpretación:** Una varianza alta indica que los datos están más dispersos respecto a la media.

---

## **4. Desviación Estándar**
La desviación estándar es la raíz cuadrada de la varianza y se expresa en las mismas unidades que los datos originales.

### **Fórmula:**
\[ \sigma = \sqrt{\sigma^2} \]

### **Ejemplo en Python:**
```python
desviacion_poblacional = np.std(datos)
desviacion_muestral = np.std(datos, ddof=1)
print(f"Desviación estándar poblacional: {desviacion_poblacional}")
print(f"Desviación estándar muestral: {desviacion_muestral}")
```

📌 **Interpretación:** Una desviación estándar alta indica mayor dispersión de los datos respecto a la media.

---

## **5. Coeficiente de Variación**
El coeficiente de variación es una medida relativa de dispersión que compara la desviación estándar con la media.

### **Fórmula:**
\[ CV = \left( \frac{\sigma}{\bar{X}} \right) \times 100 \]

### **Ejemplo en Python:**
```python
cv = (desviacion_muestral / np.mean(datos)) * 100
print(f"Coeficiente de variación: {cv}%")
```

📌 **Interpretación:** Un coeficiente de variación alto indica mayor variabilidad relativa.

---


## **4. Cuartiles y Percentiles**  

### 🔹 **Cuartiles**  
Dividen los datos en cuatro partes iguales.  
- **Q1 (25%)**: Primer cuartil  
- **Q2 (50%)**: Mediana  
- **Q3 (75%)**: Tercer cuartil  

```python
q1 = np.percentile(datos, 25)
q2 = np.percentile(datos, 50)
q3 = np.percentile(datos, 75)

print(f"Q1: {q1}, Q2 (mediana): {q2}, Q3: {q3}")
```

📌 **Ejemplo:** Si **Q1 = $1000** y **Q3 = $3000**, significa que el 50% de las personas gana entre $1000 y $3000.  

### 🔹 **Percentiles**  
Indican la posición de un dato dentro del conjunto.  

```python
percentil_90 = np.percentile(datos, 90)
print(f"El percentil 90 es: {percentil_90}")
```

📌 **Ejemplo:** Si el percentil 90 de la altura de los estudiantes es **1.85 m**, significa que el **90% mide menos de 1.85 m** y solo el **10% es más alto**.  

---

## **5. Visualización de Datos**  

### 🔹 **Histograma**  
Muestra cómo se distribuyen los datos.  

```python
import matplotlib.pyplot as plt

plt.hist(datos, bins=5, edgecolor='black')
plt.title("Histograma de datos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
```

📌 **Ejemplo:** En un histograma de sueldos, si la mayoría de las personas ganan entre $1000 y $2000, la barra en ese rango será la más alta.  

### 🔹 **Boxplot (Diagrama de Cajas)**  
Muestra cuartiles, valores atípicos y la dispersión de los datos.  

```python
import seaborn as sns

sns.boxplot(datos)
plt.title("Diagrama de cajas")
plt.show()
```

📌 **Interpretación:** Si un punto está fuera de los "bigotes" del boxplot, es un valor atípico.  

---

## **6. Ejercicios Prácticos**  

1️⃣ Crea una lista de datos con los precios de productos en un supermercado y calcula la **media, mediana y moda**.  

2️⃣ Usa NumPy para calcular la **varianza y desviación estándar** de los tiempos de espera en un restaurante.  

3️⃣ Genera una muestra aleatoria de 100 valores y construye su **histograma y boxplot**.  

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generar datos aleatorios
datos_random = np.random.normal(loc=50, scale=10, size=100)  # Media=50, Desviación=10

# Histograma
plt.hist(datos_random, bins=10, edgecolor="black")
plt.title("Histograma de datos aleatorios")
plt.show()

# Boxplot
sns.boxplot(datos_random)
plt.title("Diagrama de cajas de datos aleatorios")
plt.show()
```

📌 **Pregunta:** ¿Cómo cambia la distribución si modificamos la media o la desviación estándar en `np.random.normal()`?  

---

## **Resumen del Módulo 1**  

✅ Aprendimos los conceptos básicos de estadística descriptiva.  
✅ Calculamos medidas de tendencia central y dispersión en Python.  
✅ Exploramos percentiles y cuartiles.  
✅ Visualizamos datos con histogramas y boxplots.  

---

📌 **Próximo módulo:** **Probabilidad y Distribuciones de Probabilidad con Python**.  

🔹 ¿Quieres agregar más ejercicios o ejemplos? 🚀