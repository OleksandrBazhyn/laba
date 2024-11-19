import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Межі інтервалу
a, b = 0, 2 * np.pi

# Наближувана функція
def f(x):
    return x**2 * np.sin(x)

# Лінійні перетворення для інтервалів
def x2t(x):
    return 2 * (x - a) / (b - a) - 1

def t2x(t):
    return a + (t + 1) * (b - a) / 2

# Косинусна функція для ортогональної системи
def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

# Вагова функція для тригонометричних функцій
def rho_trigonometric(t):
    return 1 / (2 * np.pi)

def scalar_product_trigonometric(f, g):
    result = 0
    intervals = [(0, np.pi), (np.pi, 2 * np.pi)]
    for (start, end) in intervals:
        part_result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), start, end, limit=50)
        result += part_result
    return result

# Обчислення коефіцієнтів наближення
def compute_approximation_coefficients(F, P, N):
    A = np.array([[scalar_product_trigonometric(P(n), P(m)) for n in range(N)] for m in range(N)])
    b = np.array([scalar_product_trigonometric(F, P(n)) for n in range(N)])
    return np.linalg.solve(A, b)


# Матриця Грама
N = 5  # Кількість функцій в базисі
P = trig_cosine
c = compute_approximation_coefficients(f, P, N)

# Функція наближення G(t)
def G(c):
    def inner(t):
        N = len(c)
        p = np.array([P(n)(t) for n in range(N)])
        return c.dot(p)
    return inner

# Функція наближення g(x)
def g(c):
    def inner(x):
        return G(c)(x2t(x))
    return inner

# Побудова графіка
ts = np.linspace(a, b, 1000)  # точки на інтервалі [a, b]

plt.figure(figsize=(10, 6))
plt.xlabel("$x$")
plt.ylabel("$f(x), g(x)$")
plt.grid(True)

plt.plot(ts, f(ts), label="$f(x) = x^2 \sin(x)$", color='blue')
plt.plot(ts, g(c)(ts), label="$g(x)$ - наближення", color='orange', linestyle='--')

plt.legend()
plt.title("Наближення функції $f(x) = x^2 \sin(x)$ за допомогою тригонометричних функцій")
plt.show()


# Наближення функції G(t) з коефіцієнтами c
def G(c):
    def inner(t):
        N = len(c)
        p = np.array([trig_cosine(n)(t) for n in range(N)])
        return c.dot(p)
    return inner

# Наближення функції g(x) з коефіцієнтами c
def g(c):
    def inner(x):
        return G(c)(x2t(x))
    return inner

# Оцінка залишку r(x)
def r(c):
    def inner(x):
        return f(x) - g(c)(x)
    return inner

def R(c):
    def inner(t):
        return f(t2x(t)) - G(c)(t)
    return inner

# Обчислення квадрату норми залишку ||r||^2
def r_squared(c):
    norm_f_squared = scalar_product_trigonometric(f, f)
    norm_sum = sum(c_n**2 * scalar_product_trigonometric(trig_cosine(n), trig_cosine(n)) for n, c_n in enumerate(c))
    return norm_f_squared - norm_sum

# Параметри для перевірки точності
eps = 0.1
N = 0
c = [0]

# Цикл для пошуку мінімальної кількості компонент
while r_squared(c) > eps:
    N += 1
    c = compute_approximation_coefficients(f, trig_cosine, N)

print(f"{N = }, {c = }")

# Перевірка похибки
error = np.abs(r_squared(c) - scalar_product_trigonometric(r(c), r(c)))
assert error < 1e-6, f"Error of {error} is too high, have you used the right formula?"