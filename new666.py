import numpy as np


def f(x):
    return (x - 3) * np.exp(x - 4) - 2 * np.cos(2 * x) - 3 * x + 8


def steffensen_method(x0, accuracy, max_iterations):
    x = x0
    for i in range(max_iterations):
        x1 = f(x)
        x2 = f(x1)
        x = x - ((x1 - x)**2) / (x2 - 2*x1 + x)
        if abs(x - x1) < accuracy:
            return x, i + 1
    return None, max_iterations


x0 = 1.0
accuracy = 1e-8
max_iterations = 100

root, iterations = steffensen_method(x0, accuracy, max_iterations)

if root is not None:
    print(f"x = {root} після {iterations} ітерацій.")
else:
    print("Steffensen's method did not converge within the specified number of iterations.")
