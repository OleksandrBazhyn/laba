import numpy as np
import matplotlib.pyplot as plt

# Задані значення
r_xd = np.array([0.8182, 0.354])
R_x = np.array([[1, 0.8182], [0.8182, 1]])
sigma_sq = 0.5

# Початкові значення
w = np.array([0.1, 0.1])
eta_values = [0.3, 1.0]
trajectory = []

# Метод найшвидшого спуску
for eta in eta_values:
    for i in range(100):
        gradient = -r_xd + np.dot(R_x, w)
        w = w - eta * gradient
        trajectory.append(w)
        print(f"Iteration {i + 1}, eta={eta}: w = {w}")

# Побудова траєкторії вектора ваг
trajectory = np.array(trajectory)
plt.figure()
plt.plot(trajectory[:, 0], trajectory[:, 1], 'o-')
plt.xlabel('w1')
plt.ylabel('w2')
plt.title('Траєкторія вектора ваг')

# Побудова графіка помилки
error = [np.dot((r_xd - np.dot(R_x, w)), (r_xd - np.dot(R_x, w))) + sigma_sq for w in trajectory]
plt.figure()
plt.plot(range(len(error)), error, 'o-')
plt.xlabel('Ітерація')
plt.ylabel('Помилка')
plt.title('Графік помилки')

plt.show()
