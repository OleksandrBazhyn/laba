"""
Кормановської Анастасії ДО-4
Варіант 1
Побудувати НСКН n-го степеня за системою алгебраїчних та тригонометричних функцій. Знайти відхилення.
а) для неперервної функції, за допомогою матриці Грама і тригонометричних
б) для функції, яка задається таблично (взяти обрану неперервну функцію та використати її 10 значень),
за допомогою матриці Грама і алгебраїчних.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a, b = 0, 2*np.pi


def f(x):
    # assert np.all(a <= x) and np.all(x <= b), \
    #     f"{a} <= {x} <= {b} must hold, have you passed the right x?"
    return x**2 * np.cos(x)


def x2t(x):
    # linearly transforms x from [a, b] to t in [-1, 1]
    return x
    # assert np.all(a <= x) and np.all(x <= b), \
    #     f"{a} <= {x} <= {b} must hold, have you passed the right x?"
    # return 2 * (x - a) / (b - a) - 1


def t2x(t):
    # linearly transforms t from [-1, 1] to x in [a, b]
    return t
    # assert np.all(-1 <= t) and np.all(t <= 1), \
    #     f"-1 <= {t} <= 1 must hold, have you passed the right t?"
    # return a + (t + 1) * (b - a) / 2


def F(t):
    # assert np.all(-1 <= t) and np.all(t <= 1), \
    #     f"-1 <= {t} <= 1 must hold, have you passed the right t?"
    return f(t2x(t))


def P(n):
    def Pn(t):
        # assert np.all(-1 <= t) and np.all(t <= 1), \
        #     f"-1 <= {t} <= 1 must hold, have you passed the right t?"
        if n % 2 == 0:
            return np.cos(n / 2 * t)
        return np.sin((n + 1) / 2 * t)

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
plt.show()


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
for n in range(1, 6):
    plt.plot(ts, trig_sine(n)(ts), label=f"$S_{n}(t) = \sin({n} t)$")
plt.legend()

plt.tight_layout()
plt.show()


def rho_trigonometric(t):
    return 1 / (2 * np.pi)


def scalar_product(f, g):
    result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), a, b)
    assert result < 1e-6 or error < 1e-6, \
        f"Error of {error} is too high, have you passed the right f and g?"
    return result


def scalar_product_trigonometric(f, g):
    result = 0
    intervals = [(0, np.pi), (np.pi, 2 * np.pi)]
    for (start, end) in intervals:
        part_result, error = quad(lambda t: f(t) * g(t) * rho_trigonometric(t), start, end, limit=50)
        result += part_result
    return result


def trig_cosine(n):
    def Tn(t):
        return np.cos(n * t)
    return Tn


def compute_approximation_coefficients(F, P, N):
    A = np.array([[scalar_product(P(n), P(m)) for n in range(N)] for m in range(N)])
    b = np.array([scalar_product(F, P(n)) for n in range(N)])
    return np.linalg.solve(A, b)


def F(t):
    return f(t)


N = 20
# P = trig_cosine
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


def G(c):
    def inner(t):
        N = len(c)
        p = np.array([trig_cosine(n)(t) for n in range(N)])
        return c.dot(p)
    return inner


def g(c):
    def inner(x):
        return G(c)(x2t(x))
    return inner


def r(c):
    def inner(x):
        return f(x) - g(c)(x)
    return inner


def R(c):
    def inner(t):
        return f(t2x(t)) - G(c)(t)
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
# assert error < 1e-6, f"Error of {error} is too high, have you used the right formula?"
