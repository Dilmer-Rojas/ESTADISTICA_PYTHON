# **Módulo 4: Pruebas de Hipótesis**

📌 **Objetivo:** Comprender el proceso de formulación y prueba de hipótesis, conocer los diferentes tipos de pruebas estadísticas y su implementación en Python.

---

## **1. Introducción a las Pruebas de Hipótesis**
Las pruebas de hipótesis son procedimientos estadísticos que nos permiten tomar decisiones basadas en muestras de datos. Se utilizan para validar suposiciones sobre poblaciones y se aplican en diversas áreas como la ciencia, la economía y la ingeniería.

### **Elementos Claves en las Pruebas de Hipótesis**
- **Hipótesis nula (H₀):** Representa la afirmación inicial, usualmente de igualdad o ausencia de efecto.
- **Hipótesis alternativa (H₁):** Plantea que existe un efecto o diferencia significativa.
- **Nivel de significancia (α):** Probabilidad de rechazar la hipótesis nula cuando es verdadera. Comúnmente 0.05 (5%).
- **Estadístico de prueba:** Valor calculado a partir de los datos de la muestra.
- **Valor p:** Probabilidad de obtener un resultado igual o más extremo que el observado bajo H₀.
- **Regla de decisión:** Si el valor p es menor que α, se rechaza H₀ en favor de H₁.

---

## **2. Tipos de Errores en Pruebas de Hipótesis**

| Error | Descripción |
|-------|-------------|
| **Error Tipo I (α)** | Rechazar H₀ cuando es verdadera (falso positivo). |
| **Error Tipo II (β)** | No rechazar H₀ cuando es falsa (falso negativo). |

💡 **Ejemplo en la Vida Real:**
- **Error Tipo I:** Un test médico indica que una persona tiene una enfermedad cuando realmente no la tiene.
- **Error Tipo II:** Un test médico no detecta una enfermedad cuando realmente la persona la tiene.

---

## **3. Tipos de Pruebas de Hipótesis**
### **3.1 Pruebas Paramétricas**
Se utilizan cuando los datos siguen una distribución específica, generalmente normal.

#### **Prueba t de Student** (Comparación de medias)
- **Para una muestra:** Comparar la media de una muestra con un valor específico.
- **Para dos muestras independientes:** Comparar medias de dos grupos diferentes.
- **Para muestras pareadas:** Comparar medias de datos relacionados (antes y después).

🔹 **Ejemplo en Python:** Prueba t para dos muestras independientes.
```python
import scipy.stats as stats
import numpy as np

# Datos de dos grupos
grupo1 = [23, 25, 28, 22, 27]
grupo2 = [30, 32, 29, 31, 33]

# Prueba t
t_stat, p_value = stats.ttest_ind(grupo1, grupo2)
print(f"Estadístico t: {t_stat}, Valor p: {p_value}")
```

📌 **Interpretación:** Si p < 0.05, hay una diferencia significativa entre los grupos.

#### **ANOVA (Análisis de Varianza)**
Se usa cuando se comparan más de dos grupos.

```python
grupo3 = [40, 42, 41, 39, 43]
F_stat, p_value = stats.f_oneway(grupo1, grupo2, grupo3)
print(f"Estadístico F: {F_stat}, Valor p: {p_value}")
```

---

### **3.2 Pruebas No Paramétricas**
Se aplican cuando los datos no cumplen con los supuestos de normalidad.

#### **Prueba de Mann-Whitney U** (Equivalente a la t para dos muestras independientes)
```python
U_stat, p_value = stats.mannwhitneyu(grupo1, grupo2)
print(f"Estadístico U: {U_stat}, Valor p: {p_value}")
```

#### **Prueba de Wilcoxon** (Para muestras pareadas)
```python
antes = [150, 160, 165, 155, 170]
despues = [145, 155, 160, 150, 165]
stat, p_value = stats.wilcoxon(antes, despues)
print(f"Estadístico: {stat}, Valor p: {p_value}")
```

#### **Prueba de Chi-Cuadrado** (Asociación entre variables categóricas)
```python
from scipy.stats import chi2_contingency

# Tabla de contingencia
tabla = [[50, 30], [20, 40]]
chi2, p, dof, expected = chi2_contingency(tabla)
print(f"Estadístico Chi-cuadrado: {chi2}, Valor p: {p}")
```

📌 **Interpretación:** Si p < 0.05, existe una asociación significativa entre las variables.

---

## **4. Aplicación de Pruebas de Hipótesis en Casos Reales**

### **Caso 1: Comparación de ingresos antes y después de una capacitación**
📌 **Pregunta:** ¿La capacitación en análisis de datos ha aumentado el salario de los empleados?

**Datos simulados:**
```python
antes = [3000, 3200, 2900, 3100, 3050]
despues = [3500, 3700, 3400, 3600, 3550]

# Prueba t para muestras pareadas
stat, p_value = stats.ttest_rel(antes, despues)
print(f"Estadístico t: {stat}, Valor p: {p_value}")
```
📌 **Interpretación:** Si p < 0.05, hay evidencia estadística de que la capacitación aumentó el salario.

### **Caso 2: Evaluación de efectividad de dos estrategias de marketing**
📌 **Pregunta:** ¿Existe una diferencia significativa en las conversiones de clientes entre dos estrategias de marketing?

**Datos simulados:**
```python
estrategia_A = [200, 220, 250, 230, 210]
estrategia_B = [180, 190, 200, 195, 185]

# Prueba t para muestras independientes
t_stat, p_value = stats.ttest_ind(estrategia_A, estrategia_B)
print(f"Estadístico t: {t_stat}, Valor p: {p_value}")
```
📌 **Interpretación:** Si p < 0.05, se concluye que una estrategia es significativamente mejor que la otra.

### **Caso 3: Asociación entre nivel educativo y salario**
📌 **Pregunta:** ¿El nivel educativo está asociado con el nivel salarial?

**Datos simulados:**
```python
tabla = [[50, 30], [20, 40]]
chi2, p, dof, expected = chi2_contingency(tabla)
print(f"Estadístico Chi-cuadrado: {chi2}, Valor p: {p}")
```
📌 **Interpretación:** Si p < 0.05, existe asociación significativa entre el nivel educativo y el salario.

---

## **5. Conclusión**
Las pruebas de hipótesis permiten validar suposiciones estadísticas y tomar decisiones basadas en datos. La elección entre pruebas paramétricas y no paramétricas depende del tipo de datos y sus distribuciones.

🚀 **Próximo paso:** Aplicación de pruebas de hipótesis en estudios avanzados y toma de decisiones en entornos reales.

