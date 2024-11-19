import sympy as sp


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
    t = sp.symbols('t')
    for i in range(rows):
        row = []
        for j in range(cols):
            my_input = input(f"Введiть елемент ({i+1}, {j+1}): ")
            row.append(sp.sympify(my_input))
        matrix_input.append(row)
    matrix = sp.Matrix(matrix_input)
    return matrix


def P_2(B, T):
    t = sp. symbols('t')
    P2 = (B.T @ B).applyfunc (lambda el: sp.integrate(el, (t, 0, T)))
    return P2


def B_v(B, T):
    t = sp. symbols('t')
    v = [sp.zeros(B.shape[1], 1)]
    Bv = [(B @ v[0]).applyfunc(lambda el: sp.integrate (el, (t, 0, T)))]
    for i in range(5):
        w = sp.randMatrix(B.shape[1], 1)
        v.append(w)
        Bv.append((B @ w).applyfunc(lambda el: sp.integrate(el, (t, 0, T))))
    return v, Bv


def B_b(B, b, T):
    t = sp.symbols('t')
    Bb = (B.T @ b).applyfunc(lambda el: sp.integrate (el, (t, 0, T)))
    return Bb


def sol2 (P2, Bb, v):
    solution = []
    for i in range(len(v)):
        solution.append(sp.simplify (P2.pinv() @ Bb + v[i] - P2.pinv() @ P2 @ v[i]))
    return [list(sp.N(x, 3)) for x in solution]


def ambiguity_check2(P2):
    return "Розв'язок однозначний." if sp.det(P2) > 0 else "Розв'язок неоднозначний. "


def acc2(b, Bb, P2, T):
    t = sp.symbols('t')
    return list(sp.N(sp.simplify((b.T @ b).applyfunc (lambda el: sp.integrate (el, (t, 0, T))))))


def main():
    try:
        t = sp.symbols('t')
        T_input = input("Введіть T [t є [0,T]): ")
        T = float(T_input)
        cols_input = input("Введіть кількість стовпців матриці B(t): ")
        cols = int(cols_input)
        rows_input = input("Введіть кількість рядків матриці B(t): ")
        rows = int(rows_input)
        print(f"Введіть елементи матриці B(t) ({rows}x{cols}): ")
        B = input_matrix(rows, cols)
        print("Введіть елементи вектора b(t): ")
        b = input_vector(rows, 'b')

        P2 = P_2(B, T)
        Bb = B_b(B, b, T)
        v, Av = B_v(B, T)

        print("Рішення за допомогою Р2:")
        print(sol2(P2, Bb, v))
        print("Перевірка неоднозначності:")
        print(ambiguity_check2(P2))
        print("Точність обчислення:")
        print(acc2(b, Bb, P2, T))

    except ValueError as e:
        print(f"Помилка: {e}. Спробуйте ще раз.")
    except Exception as e:
        print(f"Непередбачена помилка: {e}. Спробуйте ще раз.")


main()
