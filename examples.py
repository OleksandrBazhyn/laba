import math


# Задана функція f(x)
def f(x):
    return (x - 3) * math.exp(x - 4) - 2 * math.cos(2 * x) - 3 * x + 8


# Функція для методу простої ітерації
def simple_iteration_method(x0, epsilon, max_iterations):
    print("Епсилон:", epsilon)
    print("x0 (початкове наближення):", x0)
    print("{:<5} {:<20} {:<20} {:<20}".format("k", "x_k", "x_k - x_(k-1)", "f(x_k)"))

    x_prev = x0
    for k in range(1, max_iterations + 1):
        x_next = (2 * math.cos(2 * x_prev) + 3 * x_prev - 8) / math.exp(x_prev - 4) + 3
        fx = f(x_next)
        print("{:<5} {:.10f} {:.10f} {:.10f}".format(k, x_next, abs(x_next - x_prev), fx))

        if abs(fx) <= epsilon or abs(x_next - x_prev) <= epsilon:
            print(f"\nКорінь знайдено після {k} ітерацій.")
            break

        x_prev = x_next
    else:
        print("\nКількість ітерацій вичерпана, розв'язок не знайдено.")


# Задаємо параметри для методу
x0 = 2.5  # Початкове наближення
epsilon = 1e-5  # Точність
max_iterations = 500  # Максимальна кількість ітерацій

# Виклик функції для методу простої ітерації
simple_iteration_method(x0, epsilon, max_iterations)
