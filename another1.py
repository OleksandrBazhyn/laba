import numpy as np
import matplotlib.pyplot as plt

# Задана функція f(x)
def f(x):
    return (x - 3) * np.exp(x - 4) - 2 * np.cos(2 * x) - 3 * x + 8

# Значення x для побудови графіка
x_values = np.linspace(0, 5, 1000)  # Встановлюємо діапазон значень x

# Розрахунок відповідних значень f(x)
y_values = f(x_values)

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = (x-3)*e^(x-4)-2*cos(2*x)-3*x+8')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.7)  # Додаткова лінія y=0 для визначення коренів
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік функції f(x)')
plt.legend()
plt.grid(True)
plt.show()
