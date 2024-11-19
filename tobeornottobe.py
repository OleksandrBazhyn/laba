"""
from scipy.optimize import root
import numpy as np

# Define the function
def equation(x):
    return ((x - 1) * np.exp(x - 4) - 8 * np.cos(2 * x)) / 3

# Find the roots using a different method (hybr)
sol = root(equation, [1, 2, 3], method='hybr')  # You can adjust the initial guesses

print("Roots of the equation:")
print(sol.x)
"""
import numpy as np


# Define the function f(x)
def f(x):
    return (x - 3) * np.exp(x - 4) - 2 * np.cos(2 * x) - 3 * x + 8


# Define the iterative function phi(x)
def phi(x):
    return (3 * np.exp(x - 4) + 2 * np.cos(2 * x) - 8) / np.exp(x - 4)


# Fixed-point iteration method
def fixed_point_iteration(initial_guess, tolerance, max_iterations):
    x = initial_guess
    iteration = 1

    while iteration <= max_iterations:
        x_next = phi(x)  # Calculate the next value using phi(x)

        # Check for convergence using tolerance
        if abs(x_next - x) < tolerance:
            print(f"Root found at x = {x_next} after {iteration} iterations.")
            return x_next

        x = x_next
        iteration += 1

    print("Did not converge within the specified number of iterations.")
    return None


# Initial guess and parameters
initial_guesses = [2, -2, 5]  # Different initial guesses
tolerance = 1e-8  # Tolerance for convergence
max_iterations = 1000  # Maximum number of iterations

# Perform fixed-point iteration for each initial guess
for guess in initial_guesses:
    root = fixed_point_iteration(guess, tolerance, max_iterations)
