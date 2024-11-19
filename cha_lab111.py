import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a, b = 0, 2 * np.pi  # інтервал [0, 2π]

def f(x):
    return x**2 * np.cos(x)

def rho_trigonometric(t):
    return 1 / (2 * np.pi)  # вагова функція

def scalar_product(f, g):
    # Інтеграл добутку функцій f і g з ваговою функцією
    result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), a, b)
    return result

# Тригонометричні функції
def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

def trig_sine(n):
    def Sn(t):
        return np.sin(n * t)
    return Sn

# Алгебраїчні поліноми
def algebraic_polynomial(n):
    def Pn(t):
        return t ** n
    return Pn

def compute_approximation_coefficients(F, P, N):
    # Обчислення коефіцієнтів наближення
    A = np.array([[scalar_product(P(n), P(m)) for n in range(N)] for m in range(N)])
    b = np.array([scalar_product(F, P(n)) for n in range(N)])
    return np.linalg.solve(A, b)

# Налаштування функції F, що наближається
def F(t):
    return f(t)

N = 20  # кількість членів наближення
P = trig_cosine  # можна змінити на trig_sine або algebraic_polynomial
c = compute_approximation_coefficients(F, P, N)

print("Коефіцієнти наближення для тригонометричної системи:", np.round(c, 2))

ts = np.linspace(0, 2 * np.pi, 1000)
approximation = sum(c[n] * P(n)(ts) for n in range(N))

plt.figure(figsize=(10, 6))
plt.plot(ts, f(ts), label="$f(x) = x^2 \cos(x)$", color='blue')
plt.plot(ts, approximation, label="Наближення за тригонометричними функціями", color='red', linestyle='--')
plt.title("Наближення функції $f(x) = x^2 \cos(x)$ тригонометричними функціями")
plt.xlabel("$x$")
plt.ylabel("$f(x)$ та наближення")
plt.legend()
plt.grid(True)
plt.show()

# Додаткові функції для обчислення відхилення та точності наближення
def G(c):
    def inner(t):
        N = len(c)
        p = np.array([trig_cosine(n)(t) for n in range(N)])
        return c.dot(p)
    return inner

def g(c):
    def inner(x):
        return G(c)(x)
    return inner

def r(c):
    def inner(x):
        return f(x) - g(c)(x)
    return inner

def r_squared(c):
    norm_f_squared = scalar_product(f, f)
    norm_sum = sum(c_n**2 * scalar_product(P(n), P(n)) for n, c_n in enumerate(c))
    return norm_f_squared - norm_sum

eps = 5
N = 0
c = [0]

while r_squared(c) > eps:
    N += 1
    c = compute_approximation_coefficients(f, P, N)

print(f"{N = }, {c = }")
error = np.abs(r_squared(c) - scalar_product(r(c), r(c)))
print(f"Похибка: {error}")
