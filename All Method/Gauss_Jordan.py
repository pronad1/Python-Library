# ===============================
# Solve Ax = b using Gauss-Jordan
# ===============================

def gauss_jordan(A, b):
    """
    Solves the linear system Ax = b using Gauss-Jordan elimination.
    :param A: Coefficient matrix (list of lists)
    :param b: Constant vector (list)
    :return: Solution vector x
    """
    n = len(A)

    # Create augmented matrix
    aug = [A[i] + [b[i]] for i in range(n)]


    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = aug[i][i]
        # print(diag,"NEXT")
        if diag == 0:
            raise ValueError("Zero pivot encountered!")
        for j in range(i, n + 1):
            aug[i][j] /= diag
            # print(aug[i][j])

        # Make all other elements in column i zero
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(i, n + 1):
                    aug[k][j] -= factor * aug[i][j]

    # Extract solution
    x = [row[-1] for row in aug]
    return x


# ===============================
# Example usage
# Solve:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
# ===============================

A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

solution = gauss_jordan(A, b)
print("Solution:", solution)