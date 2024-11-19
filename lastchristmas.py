import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Параметри інтервалу
a, b = 0, 2 * np.pi

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


# Наближувана функція
def f(x):
    assert np.all(a <= x) and np.all(x <= b), \
        f"{a} <= {x} <= {b} must hold, have you passed the right x?"
    return x**2 * np.cos(x)

# Вагова функція для тригонометричних функцій
def rho_trigonometric(t):
    return 1 / (2 * np.pi)

# Скалярний добуток для тригонометричних функцій
def scalar_product_trigonometric(f, g):
    result = 0
    intervals = [(0, np.pi), (np.pi, 2 * np.pi)]
    for (start, end) in intervals:
        part_result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), start, end, limit=50)
        result += part_result
    return result

# Функція для створення косинусної системи
def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

# Функція для обчислення коефіцієнтів наближення
def compute_approximation_coefficients(F, P, N):
    # Матриця Грама для косинусної системи
    A = np.array([[scalar_product_trigonometric(P(n), P(m)) for n in range(N)] for m in range(N)])
    # Вектор правих частин для наближуваної функції
    b = np.array([scalar_product_trigonometric(F, P(n)) for n in range(N)])
    # Розв'язання системи рівнянь
    return np.linalg.solve(A, b)

# Функція, що представляє нашу наближену функцію F(t)
def F(t):
    return f(t)

# Створення системи косинусних функцій і обчислення коефіцієнтів
N = 5  # Ступінь наближення
P = trig_cosine
c = compute_approximation_coefficients(F, P, N)

print("Коефіцієнти наближення для тригонометричної системи:", np.round(c, 2))

# Побудова графіка функції f(x) та наближення
ts = np.linspace(0, 2 * np.pi, 1000)
approximation = sum(c[n] * trig_cosine(n)(ts) for n in range(N))

plt.figure(figsize=(10, 6))
plt.plot(ts, f(ts), label="$f(x) = x^2 \cos(x)$", color='blue')
plt.plot(ts, approximation, label="Наближення за тригонометричними функціями", color='red', linestyle='--')
plt.title("Наближення функції $f(x) = x^2 \cos(x)$ тригонометричними функціями")
plt.xlabel("$x$")
plt.ylabel("$f(x)$ та наближення")
plt.legend()
plt.grid(True)
plt.show()
# =======================


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

plt.plot(ts, f(ts), label="$f(x) = x^2 \cos(x)$", color='blue')
plt.plot(ts, g(c)(ts), label="$g(x)$ - наближення", color='orange', linestyle='--')

plt.legend()
plt.title("Наближення функції $f(x)$ за допомогою тригонометричних функцій")
plt.show()
# =====================
# Графіки для алгебраїчних поліномів і тригонометричних функцій
def algebraic_polynomial(n):
    def Pn(t):
        return t ** n
    return Pn

def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn

def trig_sine(n):
    def Sn(t):
        return np.sin(n * t)
    return Sn

# Алгебраїчні поліноми
plt.figure(figsize=(8, 6))
plt.title("Алгебраїчні поліноми $P_n(t) = t^n$ на інтервалі $[-1, 1]$")
plt.xlabel("$t$")
plt.ylabel("$P_n(t)$")
plt.grid(True)
ts = np.linspace(-1, 1, 1000)
for n in range(5):
    plt.plot(ts, algebraic_polynomial(n)(ts), label=f"$P_{n}(t) = t^{n}$")
plt.legend()


# Тригонометричні функції (косинус і синус)
ts = np.linspace(-1, 1, 1000)
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
# plt.show()


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


def r_squared(c):
    # Обчислення норми f^2
    f_norm_squared = scalar_product_trigonometric(F, F)

    # Обчислення залишкової суми
    residual_sum = 0
    for n in range(len(c)):
        Pn_norm_squared = scalar_product_trigonometric(P(n), P(n))
        residual_sum += c[n] ** 2 * Pn_norm_squared

    # Обчислення залишку
    r_squared_value = f_norm_squared - residual_sum

    # Вивід проміжних значень для діагностики
    print(f"f_norm_squared = {f_norm_squared}")
    print(f"residual_sum = {residual_sum}")
    print(f"r_squared_value = {r_squared_value}")

    return r_squared_value
r_squared(c)

eps = 0.1
N = 0
c = []

while r_squared(c) < eps:
    # Обчислення нового коефіцієнта для збільшеного N
    new_coefficients = compute_approximation_coefficients(F, P, N + 1)

    # Додаємо лише останній обчислений коефіцієнт
    c.append(new_coefficients[-1])

    # Збільшуємо N
    N += 1

print(f"{N = }, {c = }")
