import matplotlib.pyplot as plt
import numpy as np


def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Implements the bisection method to find a root of f(x) = 0.

    Args:
        f (function): The function for which to find the root.
        a (float): The lower bound of the initial interval.
        b (float): The upper bound of the initial interval.
        tol (float): The tolerance for the approximate root.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The approximate root.
        list: A list of dictionaries containing iteration data for tabular output.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Initial interval does not bracket a root.")

    iterations_data = []

    plt.figure(figsize=(10, 6))
    x_vals = np.linspace(min(a, b) - 1, max(a, b) + 1, 400)
    plt.plot(x_vals, f(x_vals), label='f(x)', color='blue')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method.py Progression')
    plt.grid(True)

    for i in range(max_iter):
        c = (a + b) / 2
        f_c = f(c)

        iterations_data.append({
            'Iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f_c
        })

        # Plotting current iteration
        plt.scatter(c, f_c, color='red', marker='o', s=50, zorder=5)
        plt.text(c, f_c, f'  Iter {i + 1}', fontsize=8, verticalalignment='bottom')
        plt.axvline(x=a, color='yellow', linestyle=':', linewidth=0.8)
        plt.axvline(x=b, color='purple', linestyle=':', linewidth=0.8)
        plt.axvline(x=c, color='red', linestyle=':', linewidth=0.8)

        if abs(f_c) < tol or (b - a) / 2 < tol:
            print(f"\nRoot found at x = {c:.6f} after {i + 1} iterations.")
            plt.legend()
            plt.show()
            return c, iterations_data

        if f(a) * f_c < 0:
            b = c
        else:
            a = c

    print("\nMaximum iterations reached. Root not found within tolerance.")
    plt.legend()
    plt.show()
    return (a + b) / 2, iterations_data


def print_tabular_data(data):
    """Prints the iteration data in a tabular format."""
    print("\n--- Bisection Method.py Iteration Table ---")
    print(f"{'Iteration':<10} | {'a':<15} | {'b':<15} | {'c':<15} | {'f(c)':<15}")
    print("-" * 75)
    for row in data:
        print(
            f"{row['Iteration']:<10} | {row['a']:<15.8f} | {row['b']:<15.8f} | {row['c']:<15.8f} | {row['f(c)']:<15.8f}")



# Example Usage:
if __name__ == "__main__":
    def my_function(x):
        return x ** 3 - 5 * x - 9


    root, data = bisection_method(my_function, 2, 3, tol=1e-6)
    print_tabular_data(data)
