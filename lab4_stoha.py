import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def indicator_function(x1, x2, x3):
    return (x1 < x2) & (x2 < x3) & ((x3 - x2) > (x2 - x1))


def compute_triple_integral(n, case='a'):
    u = np.random.uniform(0, 1, size=(n, 3))
    x = np.sort(u, axis=1)
    x1 = x[:, 0]
    x2 = x[:, 1]
    x3 = x[:, 2]

    mask = indicator_function(x1, x2, x3)

    integrand = ((x2 + x3) / 2) ** 2

    if case == 'a':
        f_values = f_a(x1) * f_a(x2) * f_a(x3)
    elif case == 'b':
        f_values = f_b(x1) * f_b(x2) * f_b(x3)
    else:
        raise ValueError("Case must be 'a' or 'b'")

    I8 = np.mean(integrand * f_values * mask)
    return I8


# Функції f(x) для випадків a) та b)
def f_a(x):
    return np.ones_like(x)  # f(x) = 1 для x ∈ (0,1)

def f_b(x):
    return (2 * (1 + x)) / 3  # f(x) = 2(1 + x)/3 для x ∈ (0,1)

# **Завдання 1 та 2**
#
# # Функція для обчислення інтегралу I = ∫₀¹ e^x dx методом Монте-Карло (випадок a)
# def compute_integral_case_a(n):
#     # Генеруємо n випадкових чисел з рівномірного розподілу на [0,1]
#     x = np.random.uniform(0, 1, n)
#     # Обчислюємо g(x) = e^x
#     gx = np.exp(x)
#     # Оцінка інтегралу як середнє значення g(x)
#     I_estimate = np.mean(gx)
#     return I_estimate
#
# # Функція для обчислення інтегралу I = ∫₀¹ e^x dx методом Монте-Карло (випадок b)
# def compute_integral_case_b(n):
#     # Визначаємо користувацький розподіл з PDF f_b(x)
#     class CustomDistribution(stats.rv_continuous):
#         def _pdf(self, x):
#             return (2 * (1 + x)) / 3
#     custom_dist = CustomDistribution(a=0, b=1)
#     # Генеруємо n випадкових чисел з користувацького розподілу
#     x = custom_dist.rvs(size=n)
#     # Обчислюємо g(x)/p(x)
#     gx_over_px = np.exp(x) * 3 / (2 * (1 + x))
#     # Оцінка інтегралу як середнє значення g(x)/p(x)
#     I_estimate = np.mean(gx_over_px)
#     return I_estimate

# Функції для обчислення інтегралу та стандартного відхилення (Завдання 2)
def compute_integral_with_accuracy_case_a(n):
    x = np.random.uniform(0, 1, n)
    gx = np.exp(x)
    I_estimate = np.mean(gx)
    std_dev = np.std(gx, ddof=1) / np.sqrt(n)
    return I_estimate, std_dev

def compute_integral_with_accuracy_case_b(n):
    class CustomDistribution(stats.rv_continuous):
        def _pdf(self, x):
            return (2 * (1 + x)) / 3
    custom_dist = CustomDistribution(a=0, b=1)
    x = custom_dist.rvs(size=n)
    gx_over_px = np.exp(x) * 3 / (2 * (1 + x))
    I_estimate = np.mean(gx_over_px)
    std_dev = np.std(gx_over_px, ddof=1) / np.sqrt(n)
    return I_estimate, std_dev

# **Завдання 3**

# Індикаторна функція для області D₄
def indicator_function(x1, x2, x3):
    return (x1 < x2) & (x2 < x3) & ((x2 - x1) < (x3 - x2))

# Функція для обчислення потрійного інтегралу I₆
def compute_triple_integral(n, case='a'):
    # Генеруємо n наборів (x1, x2, x3)
    u = np.random.uniform(0, 1, size=(n, 3))
    x = np.sort(u, axis=1)  # Сортуємо для забезпечення x1 < x2 < x3
    x1 = x[:, 0]
    x2 = x[:, 1]
    x3 = x[:, 2]

    # Застосовуємо індикаторну функцію для області D₄
    mask = indicator_function(x1, x2, x3)

    # Обчислюємо інтегранд
    integrand = ((x1 + x2) / 2) ** 2

    if case == 'a':
        f_values = f_a(x1) * f_a(x2) * f_a(x3)
    elif case == 'b':
        f_values = f_b(x1) * f_b(x2) * f_b(x3)
    else:
        raise ValueError("Case must be 'a' or 'b'")

    # Застосовуємо маску області D₄
    v = integrand * f_values * mask

    # Оцінка інтегралу
    estimate = np.mean(v)
    return estimate

# Функція для обчислення інтегралу та стандартного відхилення для Завдання 3
def compute_triple_integral_with_accuracy(n, case='a'):
    # Генеруємо n наборів (x1, x2, x3)
    u = np.random.uniform(0, 1, size=(n, 3))
    x = np.sort(u, axis=1)
    x1 = x[:, 0]
    x2 = x[:, 1]
    x3 = x[:, 2]

    # Застосовуємо індикаторну функцію для області D₄
    mask = indicator_function(x1, x2, x3)

    # Обчислюємо інтегранд
    integrand = ((x1 + x2) / 2) ** 2

    if case == 'a':
        f_values = f_a(x1) * f_a(x2) * f_a(x3)
    elif case == 'b':
        f_values = f_b(x1) * f_b(x2) * f_b(x3)
    else:
        raise ValueError("Case must be 'a' or 'b'")

    # Застосовуємо маску області D₄
    v = integrand * f_values * mask

    # Оцінка інтегралу та стандартного відхилення
    estimate = np.mean(v)
    std_dev = np.std(v, ddof=1) / np.sqrt(n)
    return estimate, std_dev


# Основна функція
def main():
    # **Завдання 1**
    print("Завдання 1: Обчислення та порівняння інтегралу I для випадків a) та b) при n = 10, 100, 1000, 10000")
    n_values = [10, 100, 1000, 10000]
    for n in n_values:
        I_a = compute_integral_case_a(n)
        I_b = compute_integral_case_b(n)
        print(f"n = {n}")
        print(f"Випадок a): I ≈ {I_a}")
        print(f"Випадок b): I ≈ {I_b}")
        print()

    # **Завдання 2**
    print("Завдання 2: Обчислення інтегралу та точності наближення для n = 100, 1000, 50000")
    n_values = [100, 1000, 50000]
    for n in n_values:
        I_a, std_a = compute_integral_with_accuracy_case_a(n)
        I_b, std_b = compute_integral_with_accuracy_case_b(n)
        print(f"n = {n}")
        print(f"Випадок a): I ≈ {I_a}, стандартне відхилення ≈ {std_a}")
        print(f"Випадок b): I ≈ {I_b}, стандартне відхилення ≈ {std_b}")
        print()

    # **Завдання 3**
    print("Завдання 3: Обчислення потрійного інтегралу I₆ для n = 100, 1000, 50000, випадки a) та b)")
    n_values = [100, 1000, 50000]
    for n in n_values:
        I_a = compute_triple_integral(n, case='a')
        I_b = compute_triple_integral(n, case='b')
        print(f"n = {n}")
        print(f"Випадок a): I ≈ {I_a}")
        print(f"Випадок b): I ≈ {I_b}")
        print()

    # **Обчислення точності наближення для Завдання 3**
    print("Обчислення точності наближення для Завдання 3")
    for n in n_values:
        I_a, std_a = compute_triple_integral_with_accuracy(n, case='a')
        I_b, std_b = compute_triple_integral_with_accuracy(n, case='b')
        print(f"n = {n}")
        print(f"Випадок a): I ≈ {I_a}, стандартне відхилення ≈ {std_a}")
        print(f"Випадок b): I ≈ {I_b}, стандартне відхилення ≈ {std_b}")
        print()

if __name__ == "__main__":
    main()