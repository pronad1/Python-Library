import matplotlib.pyplot as plt
import numpy as np

def bisection_method(f,a,b,tol=1e-6,max_iter=100):
    if f(a)*f(b) < 0:
        print("Initial interval does not bracket a root.")

    iteration_data=[]

    plt.figure(figsize=(10,6))
    x_valus=np.linspace(min(a,b)-1,max(a,b)+1,400)
    plt.plot(x_valus,f(x_valus),label='f(x)',color='blue')
    plt.axhline(0,clor='black',linestyle='--',linwidth=0.8)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method.py Progression')
    plt.grid(True)

    for i in range(max_iter):
        c=(a+b)/2
        f_c=f(c)

        iteration_data.append({
            'Iteration': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f_c': f_c,
        })

        if abs(f_c)<tol or (b-a)/2<tol:
            print(f"\nRoot found at x={c:.6f} after {i+1}th iteration.")
            plt.legend()
            plt.show()
            return c, iteration_data


        if f(a)*f_c<0:
            b=c
        else:
            a=c
    print(f"Maximum iteration reached. Root not found within tolerance.")
    plt.legend()
    plt.show()
    return (a+b)/2, iteration_data


def print_tabular_method(data):
    print("\n----Bisection Method.py Iteration Table----")
    print(f"{'Iteration':<10} | {'Lower Bound':<15} | {'Upper Bound':<15} | {'Mid Point':<15} | {'f(c):<15'}")
    print('-'*75)
    for row in data:
        print(f"{row['Iteration']:<10} | {row['a']:<15.8f} | {row['b']:<15.8f} | {row['c']:<15.8f} | {row['f(c)']:<15.8f}")





if __name__ == '__main__':
    def my_function(x):
        return x**3 - 5*x - 9

    root, data = bisection_method(my_function,2,3)
    print_tabular_method(data)