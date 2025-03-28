# **Módulo 2: Probabilidad y Distribuciones de Probabilidad**

📌 **Objetivo:** Comprender los conceptos fundamentales de la probabilidad y las distribuciones estadísticas, así como su implementación en Python.

---

## **1. Fundamentos de Probabilidad**

La probabilidad mide la posibilidad de ocurrencia de un evento dentro de un espacio muestral. Se expresa en valores entre 0 y 1, donde 0 indica imposibilidad y 1 certeza absoluta.

### **1.1 Espacio Muestral y Eventos**

- **Espacio muestral (Ω):** Conjunto de todos los posibles resultados de un experimento.
- **Evento (E):** Subconjunto del espacio muestral que contiene los resultados favorables.
- **Probabilidad de un evento:** Se calcula como:
  
  \[
  P(E) = \frac{\text{Casos favorables}}{\text{Casos posibles}}
  \]
  
### **1.2 Reglas de Probabilidad**

1. **Regla de la suma:** Si A y B son eventos mutuamente excluyentes:
   \[
   P(A \cup B) = P(A) + P(B)
   \]
2. **Regla del complemento:** La probabilidad de que un evento no ocurra es:
   \[
   P(A^c) = 1 - P(A)
   \]
3. **Regla del producto:** Si A y B son eventos independientes:
   \[
   P(A \cap B) = P(A) \cdot P(B)
   \]

### **Ejemplo en Python: Simulación de Lanzamiento de un Dado**
```python
import numpy as np

lanzamientos = np.random.randint(1, 7, 10000)  # Simulación de 10,000 lanzamientos
prob_3 = np.sum(lanzamientos == 3) / len(lanzamientos)
print(f"Probabilidad de obtener un 3: {prob_3:.4f}")
```

📌 **Interpretación:** Cuanto mayor sea el número de simulaciones, más se aproximará la probabilidad a 1/6.

---

## **2. Probabilidad Condicional y Teorema de Bayes**

La probabilidad condicional es la probabilidad de que ocurra un evento A dado que ya ocurrió un evento B.

### **2.1 Fórmula de Probabilidad Condicional**
\[
P(A | B) = \frac{P(A \cap B)}{P(B)}
\]

### **2.2 Teorema de Bayes**
Usado para actualizar probabilidades con información nueva:
\[
P(A | B) = \frac{P(B | A) P(A)}{P(B)}
\]

### **Ejemplo en Python: Clasificación Bayesiana**
```python
from scipy.stats import norm

# Supongamos que la probabilidad de tener una enfermedad es del 1%
P_A = 0.01  # P(E)
P_no_A = 0.99  # P(no E)

# Sensibilidad y especificidad del test
P_B_dado_A = 0.95  # P(Positivo | Enfermo)
P_B_dado_no_A = 0.05  # P(Positivo | No Enfermo)

# Probabilidad total de dar positivo
P_B = P_B_dado_A * P_A + P_B_dado_no_A * P_no_A

# Probabilidad de estar enfermo dado un test positivo (Teorema de Bayes)
P_A_dado_B = (P_B_dado_A * P_A) / P_B
print(f"Probabilidad de estar enfermo dado un test positivo: {P_A_dado_B:.4f}")
```

📌 **Interpretación:** A pesar de un test positivo, la probabilidad real de estar enfermo puede ser baja si la enfermedad es rara.

---

## **3. Distribuciones de Probabilidad**

Las distribuciones describen cómo se comportan los datos en un fenómeno aleatorio.

### **3.1 Distribución Uniforme**
Cada resultado tiene la misma probabilidad de ocurrir.
```python
import matplotlib.pyplot as plt
import scipy.stats as stats

datos = np.random.uniform(0, 1, 10000)
plt.hist(datos, bins=20, density=True, alpha=0.6, color='g')
plt.title('Distribución Uniforme')
plt.show()
```

### **3.2 Distribución Normal (Gaussiana)**
Caracterizada por su media y desviación estándar.
```python
datos = np.random.normal(loc=0, scale=1, size=10000)
plt.hist(datos, bins=30, density=True, alpha=0.6, color='b')
plt.title('Distribución Normal')
plt.show()
```

📌 **Interpretación:** Muchos fenómenos naturales siguen una distribución normal (altura, peso, etc.).

### **3.3 Distribución Binomial**
Modela el número de éxitos en una cantidad fija de ensayos independientes.
```python
n, p = 10, 0.5  # 10 ensayos, probabilidad de éxito 0.5
datos = np.random.binomial(n, p, 10000)
plt.hist(datos, bins=10, density=True, alpha=0.6, color='r')
plt.title('Distribución Binomial')
plt.show()
```

### **3.4 Distribución de Poisson**
Modela eventos raros en un intervalo de tiempo fijo.
```python
lambda_ = 4
datos = np.random.poisson(lambda_, 10000)
plt.hist(datos, bins=15, density=True, alpha=0.6, color='purple')
plt.title('Distribución de Poisson')
plt.show()
```

---

## **4. Prueba de Normalidad de Datos**

Determina si un conjunto de datos sigue una distribución normal.

### **4.1 Curtosis y Asimetría**
```python
from scipy.stats import skew, kurtosis

datos = np.random.normal(0, 1, 1000)
print(f"Asimetría: {skew(datos):.4f}")
print(f"Curtosis: {kurtosis(datos):.4f}")
```

### **4.2 Test de Shapiro-Wilk**
```python
from scipy.stats import shapiro

stat, p = shapiro(datos)
print(f"p-valor: {p:.4f}")
```
📌 **Interpretación:** Si el p-valor es menor que 0.05, los datos no siguen una distribución normal.

---

## **5. Simulación de Probabilidades en Python**

### **5.1 Generación de valores aleatorios**
```python
dados = np.random.choice([1, 2, 3, 4, 5, 6], size=10000)
plt.hist(dados, bins=6, density=True, alpha=0.6, color='orange')
plt.title('Simulación de lanzamiento de un dado')
plt.show()
```



