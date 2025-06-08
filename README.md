# Método de Newton-Raphson para Resolver Ecuaciones No Lineales

Este repositorio contiene una implementación en Python del método de Newton-Raphson para encontrar la raíz de una ecuación no lineal

---

## 📌 Descripción

El código utiliza el método iterativo de Newton-Raphson para aproximar la solución de la ecuación dada, partiendo de una estimación inicial (`t0 = 432`). El algoritmo calcula en cada iteración:

- El valor de la función \( f(t) \) y su derivada \( f'(t) \).
- Una nueva aproximación de la raíz.
- El error relativo entre iteraciones consecutivas.

El proceso se detiene cuando el error relativo es menor a una tolerancia definida (`tol = 0.002`) o se alcanza el número máximo de iteraciones (`max_iter = 100`).

---

## 📂 Estructura del Código

- `newton_raphson.py`: Implementación principal del método.

### Contiene:

- Función `f(t)`: Define la ecuación a resolver.
- Función `df(t)`: Calcula la derivada analítica de `f(t)`.
- Función `newton_raphson(t0, tol, max_iter)`: Ejecuta el algoritmo y devuelve los resultados por iteración.
- Salida detallada en consola (valor actual, siguiente aproximación, error, etc.).

## 📊 Ejemplo de Salida
```bash
Iteración 1:
  x_n = 432.0000
  f(x_n) = 2.6866e+139
  f'(x_n) = 2.0356e+139
  x_(n+1) = 430.6802
  Error relativo = 0.003064

Iteración 2:
  x_n = 430.6802
  f(x_n) = 1.9443e+139
  f'(x_n) = 1.4738e+139
  x_(n+1) = 429.4609
  Error relativo = 0.002839
```
---

## 📜 Licencia [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

<div style="
    background: linear-gradient(90deg, #e8e8e8 100%);
    border-left: 4px solid #3498db;
    padding: 1rem;
    border-radius: 4px;
    margin: 1rem 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
">

Este proyecto está licenciado bajo **Apache License 2.0**.  
Para más información, consulta el archivo [LICENSE](LICENSE) o visita [apache.org/licenses](https://www.apache.org/licenses/LICENSE-2.0).
</div>

<h2>
  ✨ Elaborado por
  <img src="https://img.shields.io/badge/Juan%20David%20Gomez-black?style=for-the-badge&logo=dev.to&logoColor=white" alt="Author" style="vertical-align: middle; margin-left: 8px;">
</h2>

[![GitHub](https://img.shields.io/badge/GitHub-JuanDavidGomezN-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/juangomezn)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-JuanDavidGomezN-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/juangomezn)

[![Gmail](https://img.shields.io/badge/Gmail-juan.david%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gomezninoj681@gmail.com)
