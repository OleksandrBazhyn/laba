import pulp


def solve_matrix_game(row_payoffs, col_payoffs):
    prob = pulp.LpProblem("Matrix_Game", pulp.LpMinimize)

    num_rows = len(row_payoffs)
    num_cols = len(col_payoffs[0])
    row_strategies = pulp.LpVariable.dicts("Row_Strategy", ((i, j) for i in range(num_rows) for j in range(num_cols)),
                                           lowBound=0)
    col_strategies = pulp.LpVariable.dicts("Col_Strategy", ((i, j) for i in range(num_rows) for j in range(num_cols)),
                                           lowBound=0)

    prob += pulp.lpSum([row_strategies[i, j] * row_payoffs[i][j] for i in range(num_rows) for j in range(num_cols)])

    for i in range(num_rows):
        prob += pulp.lpSum([row_strategies[i, j] for j in range(num_cols)]) == 1

    for j in range(num_cols):
        prob += pulp.lpSum([col_strategies[i, j] for i in range(num_rows)]) == 1

    prob.solve()

    row_optimal_strategy = [[pulp.value(row_strategies[i, j]) for j in range(num_cols)] for i in range(num_rows)]
    col_optimal_strategy = [[pulp.value(col_strategies[i, j]) for j in range(num_cols)] for i in range(num_rows)]
    optimal_value = pulp.value(prob.objective)

    return row_optimal_strategy, col_optimal_strategy, optimal_value


row_payoffs = [[-1, 1], [1, -1]]
col_payoffs = [[1, -1],[-1, 1]]

row_optimal_strategy, col_optimal_strategy, optimal_value = solve_matrix_game(row_payoffs, col_payoffs)

print("Оптимальні стратегії першого гравця:")
for row in row_optimal_strategy:
    print(row)
print("Оптимальні стратегії другого гравця:")
for row in col_optimal_strategy:
    print(row)
print("Оптимальний виграш:", optimal_value)
