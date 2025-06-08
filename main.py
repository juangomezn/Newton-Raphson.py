import math

# Definir la función f(t) = (3e^(0.76t))/(10t) - 115
def f(t):
    return (3 * math.exp(0.76 * t)) / (10 * t) - 115

# Derivada de la función f'(t) = [3e^(0.76t)(0.76t - 1)] / (10t²)
def df(t):
    return (3 * math.exp(0.76 * t) * (0.76 * t - 1)) / (10 * t ** 2)

# Método de Newton-Raphson
def newton_raphson(t0, tol=0.002, max_iter=100):
    results = []  # Lista para guardar los resultados de cada iteración
    t = t0
    for i in range(max_iter):
        ft = f(t)
        dft = df(t)

        if dft == 0:  # Evitar división por cero
            print("Derivada cero. El método falla.")
            break

        # Calcular la nueva aproximación
        t_next = t - ft / dft
        # Calcular el error relativo
        error = abs((t_next - t) / t_next)

        # Guardar la iteración en la lista
        results.append((i + 1, t, ft, dft, t_next, error))

        # Verificar si el error está dentro del criterio
        if error < tol:
            break

        # Actualizar t para la siguiente iteración
        t = t_next

    return results

# Ejecutar el método con una estimación inicial de 432 horas
t0 = 432
iteraciones = newton_raphson(t0)

# Mostrar los resultados
for iteracion in iteraciones:
    i, x_n, fxn, dfxn, x_next, error = iteracion
    print(f"Iteracion {i}:")
    print(f"  x_n = {x_n:.4f}")
    print(f"  f(x_n) = {fxn:.4e}")
    print(f"  f'(x_n) = {dfxn:.4e}")
    print(f"  x_(n+1) = {x_next:.4f}")
    print(f"  Error relativo = {error:.6f}\n")