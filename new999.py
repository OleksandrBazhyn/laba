import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Define the function F(x)
def F(x):
    return x[0]**2 + 25*x[1]**2

# Define the gradient of the function F(x)
def grad_F(x):
    return np.array([2*x[0], 50*x[1]])

# Initial guess
x0 = np.array([-1, -2.5])

# Compute the gradient at the initial point
grad_x0 = grad_F(x0)

# Minimize the function using the Brent method
res = minimize_scalar(lambda alpha: F(x0 - alpha*grad_x0), bounds=(0, 1), method='bounded')

# Minimum point
x_min = x0 - res.x * grad_x0

# Contour plot of the function F(x) and the search trajectory for the minimum
x = np.linspace(-2, 2, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
Z = X**2 + 25*Y**2
plt.contour(X, Y, Z, levels=np.logspace(0, 3, 20))
plt.plot(x_min[0], x_min[1], 'ro') # Minimum point
plt.annotate('Minimum', (x_min[0], x_min[1]), textcoords="offset points", xytext=(-10, -10), ha='center')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Search trajectory for the minimum')
plt.show()