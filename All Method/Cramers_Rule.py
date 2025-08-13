import numpy as np


# ===============================
# Solve Ax = b using Cramer's Rule
# ===============================

def cramer_rule(A, b):
    """
    Solves the linear system Ax = b using Cramer's Rule.
    :param A: Coefficient matrix (numpy array)
    :param b: Constant vector (numpy array)
    :return: Solution vector x
    """
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("Determinant is zero, system has no unique solution!")

    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b  # Replace i-th column with constants
        x[i] = np.linalg.det(Ai) / det_A

    return x


# ===============================
# Example usage
# Solve:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
# ===============================

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)

solution = cramer_rule(A, b)
print("Solution:", solution)
