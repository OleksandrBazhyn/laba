import numpy as np


def read_matrix_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            matrix = np.loadtxt(file)
        return matrix
    except Exception as e:
        print("Помилка при зчитуванні матриці:", e)
        return None


def read_vector_from_file(file_path):
    try:
        vector = np.loadtxt(file_path)
        return vector
    except Exception as e:
        print("Помилка при зчитуванні вектора:", e)
        return None


def check_determinant(matrix):
    det = np.linalg.det(matrix)
    if det == 0:
        print("Визначник матриці дорівнює 0.")
        return False
    return True


def check_1_7(matrix):
    ATA = matrix.T @ matrix
    det_ATA = np.linalg.det(ATA)
    if det_ATA > 0:
        return True
    else:
        print("Умова 1.7 не виконується: det(A^T A) ≤ 0.")
        return False


def pseudoinverse(matrix):
    return np.linalg.pinv(matrix)


def solve_for_x_hat(A, b):
    A_plus = pseudoinverse(A)
    x_hat = A_plus @ b
    return x_hat


def compute_epsilon_squared(A, b):
    A_plus = pseudoinverse(A)
    epsilon_squared = b.T @ b - b.T @ A @ A_plus @ b
    return epsilon_squared


def main():
    matrix_file = 'C:/Users/miy_PC/PycharmProjects/pythonProject/matrix.txt'
    vector_file = 'C:/Users/miy_PC/PycharmProjects/pythonProject/vector.txt'

    A = read_matrix_from_file(matrix_file)
    b = read_vector_from_file(vector_file)

    if A is None:
        return
    if b is None:
        return



    if not check_1_7(A):
        return

    x_hat = solve_for_x_hat(A, b)
    print("Розв'язок для вектора x̂:", x_hat)

    epsilon_squared = compute_epsilon_squared(A, b)
    print("Точність ε²:", epsilon_squared)


main()