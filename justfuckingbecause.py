import numpy as np

n = 7
A = np.zeros((n, n), dtype=np.float64)
for i in range (n):
    for j in range(n):
        if i == j:
            A[i][j] = 10 + 4/(i+1)
        elif j == i + 1:
            A[i][j] = 1
        elif j == i-1:
            A[i][j] = 1
        elif (i == 0 and j == n-1) or (i == n-1 and j == 0):
            A[i][j] = 4
A[n-1, n-2] = 5
A[n-2, n-1] = 5
A[0, 1] = 4
A[1, 0] = 4

print("A = ")

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or j == n // 2 or i == n // 2 or \
           i in [0, n - 1, 1, n - 2, 2, n - 3, 3, n - 4] and j in [0, n - 1, 1, n - 2, 2, n - 3, 3, n - 4] or \
           (i == 2 and j == 4) or (i == 4 and j == 2) or (i == 3 and j == 5) or (i == 5 and j == 3) or \
           (i == 1 and j == 6) or (i == 6 and j == 1) or (i == 4 and j == 6) or (i == 6 and j == 4):
            print(f"{A[i][j]:>12.{8}f}", end=" ")
        else:
            print(f"{'':>12s}", end=" ")
    print()


b = np.zeros((n, 1), dtype=np.float64)

for i in range(n):
    b[i] = n + 3 - i

print("b = \n", b)

print('\n=============№1=============\n')

is_symmetric = np.array_equal(A, A.T)

if is_symmetric:
    print("The matrix A is symmetric.")
else:
    print("The matrix A is not symmetric.")

print('\n=============№2=============\n')

S = np.zeros((n, n))
D = np.zeros((n, n))

for i in range(n):
    sum = 0
    for p in range(i):
        sum += (S[p][i] ** 2) * D[p][p]
    D[i][i] = np.sign(A[i][i] - sum)
    S[i][i] = np.sqrt(np.abs (A[i][i] - sum))
    for j in range(i+1, n):
        sum = 0
    for p in range(i):
        sum += S[p][i] * D[p][p] * S[p][j]
    S[i][j] = (A[i][j] - sum)/(S[i][i] * D[i][i])

print("S = \n", S)
print("\nD = \n", D)

print('\n=============№3=============\n')
STD = np.dot(S.T, D)
n = STD.shape[0]
y = np.zeros(n)

for i in range(n-1, -1, -1):
    y[i] = b[i] / STD[i][i]
    for j in range(i-1, -1, -1):
        b[j] -= STD[j][i] * y[i]

print("y = ")
print("[")
for element in np.array(y):
    print(f"{element:.8f}")
print("]")

"""
n = S.shape[0] 
m = D.shape[1]  

ST = np.transpose(S)

STD = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        total = 0
        for k in range(n):
            total += ST[i][k] * D[k][j]
        STD[i][j] = total

y = np.zeros((m,))
for i in range(m):
    total = 0
    for j in range(n):
        total += STD[j][i] * b[j]
    y[i] = total

print("y = \n")
y = np.zeros((n, 1), dtype=np.float64)
print(y)

print("========")

STD = np.dot(S.T, D)
y = np.linalg.solve(STD, b)
print("y = ")
print(y)

print("==============")
"""
print('\n=============№4=============\n')

n = S.shape[0]
x = np.zeros(n)

for i in range(n-1, -1, -1):
    x[i] = y[i] / S[i][i]
    for j in range(i-1, -1, -1):
        y[j] -= S[j][i] * x[i]

print("розв'язок системи x = ")

print("[")
for element in np.array(x):
    print(f"{element:.8f}")
print("]")

# print("Перевірка Ax = b:", np.dot(A, x), " = \n", b)
print("Вектор нев'язки: r = ", np.dot(A,x) - b)

print("======================")

print("cond(A) = ", np.linalg.cond(A))

print("======================")

print("det(A) = ", np.linalg.det(A))

"""
det = float(1)
for i in range(n):
    det *= D[i][i]
for i in range(n):
    det *= S[i][i]**2

print(det)
"""
print("======================")
A1 = np.linalg.inv(A)
print("A^-1 = ", A1)
print("\n A*A^-1 = \n", A*A1)
print("======================")

"""
def gaus_solve(L, U, y):
    n = len(y)

    # Forward substitution to solve Ly = b
    for i in range(n):
        y[i] = y[i] / L[i][i]
        L[i][i] = 1
        for j in range(i + 1, n):
            y[j] -= y[i] * L[j][i]
            L[j][i] = 0

    # Backward substitution to solve Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] / U[i][i]
        U[i][i] = 1
        for j in range(i - 1, -1, -1):
            y[j] -= x[i] * U[j][i]
            U[j][i] = 0
    return x


A_inv = np.zeros((n, n))
for i in range(n):
    e = np. zeros((n, 1))
    e[i] = 1
    y = gaus_solve(L.copy(), U.copy(), e.copy())
    for j in range(n):
        A_inv[i][j] = y[j]

"""
print("==------метод зейделя-------==")
L = np.tril(A)
U = A - L

M = np.dot(np.linalg.inv(L), U)
spectral_radius = np.max(np.abs(np.linalg.eigvals(M)))

print(f"Спектральний радіус матриці переходу: {spectral_radius}")

# Перевірка збіжності: якщо спектральний радіус < 1, то метод Зейделя збігається
if spectral_radius < 1:
    print("Метод Зейделя збігається для даної матриці A.")
else:
    print("Метод Зейделя не збігається для даної матриці A.")

print("00000000000000000000000000000000")
"""A = np.copy(A0)
    L = np.tril(A)
    U = A - L
    A2 = np.dot(np.linalg.inv(L), U)
    if np.linalg.norm(A2) >= 1:
        print(np.linalg.norm(A2))
        raise ValueError("(L+D)^-1*U >- 1, method is not convergent")"""

def gauss_seidel_solve(A0, b):
    eps = 0.000001
    n = len(A)
    x = np.zeros_like(b)
    i = 0
    converge = False
    while(not converge):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.sum([A[i][j] * x_new[j] for j in range(i)])
            s2 = np.sum([A[i][j] * x[j] for j in range(i + 1, n)])
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        converge = np.linalg.norm(x_new - x) <= eps
        x = x_new
        i += 1
    return x, і


x, i = gauss_seidel_solve(A, b)
print("x = \n", x)

print("Вектор нев'язки: г = \n", np.dot (A, x) - b)
print("Кількість ітерацій: ", і)
