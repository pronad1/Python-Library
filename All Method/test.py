import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 4 * x +1
def g(x):
    return (x**3+1)/4

def iteration(g,x,tol=1e-5,max_iter=100):
    for i in range(max_iter):
        x_new=g(x)
        if abs(x_new - x)<tol:
            return x_new
        x=x_new
    raise ValueError("Did not converge within the maximum number of iterations")

root= iteration(g,1)
print("The root is:", root)

x=np.arange(-10,10,0.2)
plt.plot(x,f(x),label='f = x^3 - 4x + 1')
plt.scatter(root,f(root),color='blue')
plt.axvline(root,color='red',linestyle='--',label=f'x = {root:.5f}')

plt.axvline(0, color='black', linestyle='--')
plt.axhline(0, color='black', linestyle='--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Iteration Method Root: {root:.5}')
plt.legend()
plt.grid(True)
plt.show()
