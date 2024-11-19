import numpy as np
from numpy import linalg as la
import sympy as sp
import random

t = sp.symbols('t')


def func(B, b, T):
    P20 = np.transpose(B) @ B
    aux = np.shape(P20)[0]
    P2 = np.array([[sp.integrate(P20[i][j], (t,0,T)) for j in range(aux)]for i in range(aux)], dtype=float)
    Bb0 = np.transpose(B) @ b
    Bb = np.array([sp.integrate(Bb0[i], (t,0,T)) for i in range(aux)], dtype=float)
    Pp = la.pinv(P2)

    x0 = Pp @ Bb

    un = []
    if la.det(P2) > 0:
        answer = "..."
    else:
        answer = "///"
    pert = np.array([random.uniform(-1, 1) for i in range(aux)])
    x = x0 + pert - Pp @ P2 @ pert
    un = [answer, pert, x]
    sqr = sp.integrate(np.transpose(b) @ b, (t, 0, T)) - np.transpose(Bb) @ Pp @ Bb
    return [x0, un, sqr]

try:
    B = np.array([[sp.sin(t), sp.sin(t)], [-sp.cos(t), sp.cos(t)], [sp.sqrt(t), t**3]])
    b = np.array([sp.sqrt(t), sp.sin(t), sp.cos(t)])
    T = 1
    res = func(B, b, T)
    s1, s2, s3 = res[0], res[1], res[2]
    print("Minimal norm: ", s1)
    print(s2[0])
    print("Perturbed: ", s2[2])
    print("square of the error: ", s3)
except BaseException as e:
    print(e)



"""
# Основна функція для обчислення
def func(B, b, T):
    P20 = np.transpose(B) @ B
    aux = np.shape(P20)[0]
    P2 = np.array([[sp.integrate(P20[i][j], (t, 0, T)) for j in range(aux)] for i in range(aux)], dtype=float)
    Bb0 = np.transpose(B) @ b
    Bb = np.array([sp.integrate(Bb0[i], (t, 0, T)) for i in range(aux)], dtype=float)
    Pp = la.pinv(P2)

    x0 = Pp @ Bb

    if la.det(P2) > 0:
        print("\nРозв'язок однозначний")
    else:
        print("\nРозв'язок неоднозначний")
    pert = np.array([random.uniform(-1, 1) for i in range(aux)])
    x = x0 + pert - Pp @ P2 @ pert
    un = [pert, x]
    sqr = sp.integrate(np.transpose(b) @ b, (t, 0, T)) - np.transpose(Bb) @ Pp @ Bb
    return [x0, un, sqr]

# Введення даних вручну
t = sp.symbols('t')
T_input = input("Введіть T [t є [0,T]): ")
T = float(T_input)  # перетворення введеного T у число
cols_input = input("Введіть кількість стовпців матриці B(t): ")
cols = int(cols_input)
rows_input = input("Введіть кількість рядків матриці B(t): ")
rows = int(rows_input)

print(f"Введіть елементи матриці B(t) ({rows}x{cols}): ")
B = input_matrix(rows, cols)
print("Введіть елементи вектора b(t): ")
b = input_vector(rows, 'b')

# Виклик функції з введеними даними
try:
    res = func(np.array(B).astype(np.object_), np.array(b).astype(np.object_), T)
    s1, s2, s3 = res[0], res[1], res[2]
    print("Minimal norm: ", s1)
    print(s2[0])
    print("Perturbed: ", s2[2])
    print("Square of the error: ", s3)
except BaseException as e:
    print(e)




def input_vector(size, name):
    vector_input = []
    t = sp.symbols('t')
    for i in range(size):
        my_input = input(f"Bведiть {i + 1} елемент вектopа {name}: ")
        vector_input.append(sp.sympify(my_input))
    vector = sp.Matrix(vector_input)
    return vector


def input_matrix(rows, cols):
    matrix_input = []
    t = sp.symbols ('t')
    for i in range(rows):
        row = []
        for j in range(cols):
            my_input = input(f"Введiть елемент ({i+1}, {j+1}): ")
            row.append(sp.sympify(my_input))
        matrix_input.append(row)
    matrix = sp.Matrix (matrix_input)
    return matrix


t = sp.symbols ('t')
T_input = input("Введіть T [t є [0,T]): ")
T = int(T_input)
cols_input = input("Введіть кількість стовпців матриці B(t): ")
cols = int(cols_input)
rows_input = input("Введіть кількість рядків матриці B(t): ")
rows = int(rows_input)

print(f"Введіть елементи матриці B(t) ({rows}+{cols}); ")
B = input_matrix(rows, cols)
b = input_vector(rows, 'b')

"""