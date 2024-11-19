import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a, b = 0, 2*np.pi


def f(x):
    assert np.all(a <= x) and np.all(x <= b), \
        f"{a} <= {x} <= {b} must hold, have you passed the right x?"
    return x**2 * np.cos(x)


def x2t(x):
    # linearly transforms x from [a, b] to t in [-1, 1]
    assert np.all(a <= x) and np.all(x <= b), \
        f"{a} <= {x} <= {b} must hold, have you passed the right x?"
    return 2 * (x - a) / (b - a) - 1


def t2x(t):
    # linearly transforms t from [-1, 1] to x in [a, b]
    assert np.all(-1 <= t) and np.all(t <= 1), \
        f"-1 <= {t} <= 1 must hold, have you passed the right t?"
    return a + (t + 1) * (b - a) / 2


def F(t):
    assert np.all(-1 <= t) and np.all(t <= 1), \
        f"-1 <= {t} <= 1 must hold, have you passed the right t?"
    return f(t2x(t))


def P(n):
    def Pn(t):
        assert np.all(-1 <= t) and np.all(t <= 1), \
            f"-1 <= {t} <= 1 must hold, have you passed the right t?"
        return np.cos(n * np.arccos(t))
    return Pn


ts = np.linspace(-1, 1, 1000)


def algebraic_polynomial(n):
    def Pn(t):
        return t ** n
    return Pn


plt.figure(figsize=(8, 6))
plt.title("Алгебраїчні поліноми $P_n(t) = t^n$ на інтервалі $[-1, 1]$")
plt.xlabel("$t$")
plt.ylabel("$P_n(t)$")
plt.grid(True)

for n in range(5):
    plt.plot(ts, algebraic_polynomial(n)(ts), label=f"$P_{n}(t) = t^{n}$")

plt.legend()


def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn


def trig_sine(n):
    def Sn(t):
        return np.sin(n * t)
    return Sn


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Косинусні функції $T_n(t) = \cos(n t)$ на інтервалі $[-1, 1]$")
plt.xlabel("$t$")
plt.ylabel("$T_n(t)$")
plt.grid(True)
for n in range(5):
    plt.plot(ts, trig_cosine(n)(ts), label=f"$T_{n}(t) = \cos({n} t)$")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Синусні функції $S_n(t) = \sin(n t)$ на інтервалі $[-1, 1]$")
plt.xlabel("$t$")
plt.ylabel("$S_n(t)$")
plt.grid(True)
for n in range(1, 6):  # починаємо з 1, оскільки sin(0*t) = 0
    plt.plot(ts, trig_sine(n)(ts), label=f"$S_{n}(t) = \sin({n} t)$")
plt.legend()

plt.tight_layout()
plt.show()


"""
# ====================================
# Функції для тригонометричних функцій
def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

def trig_sine(n):
    def Sn(t):
        return np.sin(n * t)
    return Sn

# Обчислення матриці скалярних добутків для косинусних функцій
G_cos = np.array([[scalar_product(trig_cosine(n), trig_cosine(m)) for n in range(5)] for m in range(5)])

# Обчислення матриці скалярних добутків для синусних функцій
G_sin = np.array([[scalar_product(trig_sine(n), trig_sine(m)) for n in range(1, 6)] for m in range(1, 6)])

print("Матриця скалярних добутків для косинусних функцій:")
print(np.round(G_cos, 2))

print("\nМатриця скалярних добутків для синусних функцій:")
print(np.round(G_sin, 2))


# Вагова функція для тригонометричних функцій
def rho_trigonometric(t):
    return 1 / (2 * np.pi)

# Скалярний добуток з ваговою функцією
def scalar_product_trigonometric(f, g):
    result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), 0, 2 * np.pi)
    return result

# Матриця Грама для перших 5 косинусних функцій
G_trigonometric = np.array([[scalar_product_trigonometric(trig_cosine(n), trig_cosine(m)) for n in range(5)] for m in range(5)])
print("Матриця Грама для тригонометричних функцій (косинус):")
print(np.round(G_trigonometric, 2))

G_trigonometric2 = np.array([[scalar_product_trigonometric(trig_sine(n), trig_sine(m)) for n in range(5)] for m in range(5)])
print("Матриця Грама для тригонометричних функцій (синус):")
print(np.round(G_trigonometric, 2))


def compute_approximation_coefficients(F, P, N):
    A = np.array([[scalar_product_trigonometric(P(n), P(m)) for n in range(N)] for m in range(N)])
    b = np.array([scalar_product_trigonometric(F, P(n)) for n in range(N)])
    # TODO: solve the equations analytically for orthogonal systems
    return np.linalg.solve(A, b)


c = compute_approximation_coefficients(F, P, 5)
print(np.round(c, 2))
"""

# Вагова функція для тригонометричних функцій
def rho_trigonometric(t):
    return 1 / (2 * np.pi)

# Скалярний добуток для тригонометричних функцій
def scalar_product_trigonometric(f, g):
    result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), 0, 2 * np.pi)
    return result

# Функція для створення косинусної системи
def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

# Наближувана функція (змінюємо під вашу конкретну функцію, наприклад, x^2 * sin(x))
def F(x):
    return x**2 * np.cos(x)

# Функція для обчислення коефіцієнтів наближення
def compute_approximation_coefficients(F, P, N):
    # Матриця Грама для косинусної системи
    A = np.array([[scalar_product_trigonometric(P(n), P(m)) for n in range(N)] for m in range(N)])
    # Вектор правих частин для наближуваної функції
    b = np.array([scalar_product_trigonometric(F, P(n)) for n in range(N)])
    # Розв'язання системи рівнянь
    return np.linalg.solve(A, b)

# Створення системи косинусних функцій і обчислення коефіцієнтів
N = 5  # Ступінь наближення
P = trig_cosine
c = compute_approximation_coefficients(F, P, N)

print("Коефіцієнти наближення:", np.round(c, 2))
