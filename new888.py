import math


# Define the function g(x)
def g(x):
    return (2 * math.cos(2 * x) - (x - 3) * math.exp(x - 4) + 8) / 3


# Initial guess
x_0 = 1.0  # You can choose a different initial value if needed
tolerance = 1e-8  # Tolerance for convergence
max_iterations = 1000  # Maximum number of iterations

# Perform iterations
for i in range(max_iterations):
    x_new = g(x_0)

    # Check for convergence
    if abs(x_new - x_0) < tolerance:
        print(f"Converged to solution: x = {x_new:.8f}")
        break

    x_0 = x_new
else:
    print("Did not converge within the maximum number of iterations")
