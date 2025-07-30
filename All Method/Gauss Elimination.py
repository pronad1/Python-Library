import numpy as np
import matplotlib.pyplot as plt

def solve_gaussian_elimination(A, b):
    """
    Solves a system of linear equations Ax = b using Gaussian elimination.

    Args:
        A (numpy.ndarray): The coefficient matrix.
        b (numpy.ndarray): The constant vector.

    Returns:
        numpy.ndarray: The solution vector x.
        None: If the system has no unique solution (e.g., singular matrix).
    """
    n = len(b)
    # Create augmented matrix
    augmented_matrix = np.hstack((A, b.reshape(-1, 1))).astype(float)

    # Forward elimination
    for i in range(n):
        # Find pivot
        if augmented_matrix[i, i] == 0:
            # Try to swap with a row below to get a non-zero pivot
            for k in range(i + 1, n):
                if augmented_matrix[k, i] != 0:
                    augmented_matrix[[i, k]] = augmented_matrix[[k, i]]
                    break
            else:
                print("No unique solution or singular matrix.")
                return None

        # Eliminate elements below the pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= factor * augmented_matrix[i, i:]

    # Back-substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if augmented_matrix[i, i] == 0:
            print("No unique solution or singular matrix.")
            return None
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])) / augmented_matrix[i, i]

    return x

def plot_2d_system(A, b, solution=None):
    """
    Plots a 2D system of linear equations and its solution.

    Args:
        A (numpy.ndarray): The 2x2 coefficient matrix.
        b (numpy.ndarray): The 2x1 constant vector.
        solution (numpy.ndarray, optional): The 2x1 solution vector.
    """
    if A.shape != (2, 2) or b.shape != (2,):
        print("Plotting is only supported for 2D systems.")
        return

    x_vals = np.linspace(-10, 10, 400)

    plt.figure(figsize=(8, 6))

    # Plot each equation
    for i in range(2):
        if A[i, 1] != 0:
            y_vals = (b[i] - A[i, 0] * x_vals) / A[i, 1]
            plt.plot(x_vals, y_vals, label=f'Equation {i+1}: {A[i,0]}x + {A[i,1]}y = {b[i]}')
        else:
            # Vertical line if y coefficient is zero
            plt.axvline(x=b[i]/A[i,0], color=f'C{i}', linestyle='--', label=f'Equation {i+1}: {A[i,0]}x = {b[i]}')

    if solution is not None:
        plt.plot(solution[0], solution[1], 'ro', markersize=8, label='Solution')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphical Representation of Linear System')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.show()

# Example Usage:
if __name__ == "__main__":
    # Define a system of linear equations:
    # 2x + y = 5
    # x - 3y = -8
    A = np.array([[2, 1],
                  [1, -3]])
    b = np.array([5, -8])

    print("Coefficient Matrix A:")
    print(A)
    print("\nConstant Vector b:")
    print(b)

    solution_x = solve_gaussian_elimination(A, b)

    if solution_x is not None:
        print("\nSolution x:")
        print(solution_x)
        plot_2d_system(A, b, solution_x)

    # Example with a larger system (no plot for > 2D)
    A_large = np.array([[1, 1, 1],
                        [0, 2, 5],
                        [2, 5, -1]])
    b_large = np.array([6, -4, 27])

    print("\nLarger System:")
    print("Coefficient Matrix A_large:")
    print(A_large)
    print("\nConstant Vector b_large:")
    print(b_large)

    solution_large = solve_gaussian_elimination(A_large, b_large)
    if solution_large is not None:
        print("\nSolution for larger system:")
        print(solution_large)