from pulp import LpMaximize, LpProblem, LpVariable


def solve_matrix_game(matrix):
    m = len(matrix)
    n = len(matrix[0])

    prob = LpProblem("Matrix_Game", LpMaximize)

    x = [[LpVariable(f'x_{i}_{j}', lowBound=0, cat='Continuous') for j in range(n)] for i in range(m)]

    prob += sum([sum([matrix[i][j] * x[i][j] for j in range(n)]) for i in range(m)])

    for i in range(m):
        prob += sum(x[i]) == 1
    for j in range(n):
        prob += sum([x[i][j] for i in range(m)]) == 1

    prob.solve()

    print("Оптимальні стратегії першого гравця:")
    for i in range(m):
        for j in range(n):
            print(f'{x[i][j].name}: {x[i][j].varValue}')
    print("Оптимальні стратегії другого гравця:")
    for j in range(n):
        for i in range(m):
            print(f'{x[i][j].name}: {x[i][j].varValue}')

    print("Оптимальний виграш першого гравця:", prob.objective.value())


matrix1 = [
    [1, -1],
    [-1, 1]
]

solve_matrix_game(matrix1)

matrix2 = [
    [5, 2, 0], [1, 4, 3], [2, 3, 1]
]

print("\n=========\n")

solve_matrix_game(matrix2)



"""
# Приклад 1: Матриця виграшів
matrix1 = np.array([[5, 3, 1], [2, 4, 6], [7, 8, 9]])
print("Приклад 1:")
solve_matrix_game(matrix1)
visualize_strategies([[0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

# Приклад 2: Матриця виграшів
matrix2 = np.array([[10, 20, 30], [15, 25, 35], [5, 15, 40]])
print("\nПриклад 2:")
solve_matrix_game(matrix2)
visualize_strategies([[0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])

# Приклад 3: Матриця виграшів
matrix3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nПриклад 3:")
solve_matrix_game(matrix3)
visualize_strategies([[1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3]])

"""