import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the function phi(x)
phi = (2*sp.cos(2*x) - 3*x + 8) / sp.exp(x - 4) + 3

# Calculate the derivative of phi(x) with respect to x
phi_derivative = sp.diff(phi, x)

# Display the derivative of phi(x)
print("Derivative of phi(x) with respect to x:")
print(phi_derivative)
