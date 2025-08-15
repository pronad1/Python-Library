import numpy as np
import matplotlib.pyplot as plt

def false_position(func, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function using the False Position method.

    Args:
        func: The function for which to find the root.
        a: The lower bound of the initial interval.
        b: The upper bound of the initial interval.
        tol: The tolerance for convergence.
        max_iter: The maximum number of iterations.

    Returns:
        The approximate root if found, otherwise None.
    """
    if func(a) * func(b) >= 0:
        print("Error: Initial guesses do not bracket a root.")
        return None

    roots = []
    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        roots.append(c)

        if abs(func(c)) < tol:
            print(f"Root found at x = {c:.6f} in {i+1} iterations.")
            return c, roots

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print("Maximum iterations reached. Root not found within tolerance.")
    return None, roots

# Example usage:
def f(x):
    return x**3 - x - 1

a = 1
b = 2
root, iterations = false_position(f, a, b)

# Plotting
if root is not None:
    x_vals = np.linspace(0, 2.5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x) = x^3 - x - 1')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8) # X-axis

    # Plot initial points
    plt.plot(a, f(a), 'ro', label=f'Initial a={a}')
    plt.plot(b, f(b), 'bo', label=f'Initial b={b}')

    # Plot iterations
    for i, r_val in enumerate(iterations):
        plt.plot(r_val, f(r_val), 'gx', markersize=8, label=f'Iteration {i+1}')
        if i < len(iterations) - 1:
            # Draw secant line for the current iteration
            x_secant = np.array([a, b])
            y_secant = np.array([f(a), f(b)])
            plt.plot(x_secant, y_secant, 'k--', linewidth=0.5)
            # Update a or b for the next secant line in the plot
            if f(r_val) * f(a) < 0:
                b = r_val
            else:
                a = r_val

    plt.plot(root, f(root), 'rx', markersize=10, label=f'Root = {root:.6f}')
    plt.title('False Position Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()