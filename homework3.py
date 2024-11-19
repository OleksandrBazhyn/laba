import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar


def F(x):
    return x[0]**2 + 25*x[1]**2


def grad_F(x):
    return np.array([2*x[0], 50*x[1]])


x0 = np.array([-1, -2.5])

grad_x0 = grad_F(x0)

res = minimize_scalar(lambda alpha: F(x0 - alpha*grad_x0), method='golden')

x_min = x0 - res.x * grad_x0

x = np.linspace(-2, 2, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
Z = X**2 + 25*Y**2
plt.contour(X, Y, Z, levels=np.logspace(0, 3, 20))
plt.plot(x_min[0], x_min[1], 'ro')
plt.annotate('Minimum', (x_min[0], x_min[1]), textcoords="offset points", xytext=(-10, -10), ha='center')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('пошук мінімуму функції F(x)')
plt.show()