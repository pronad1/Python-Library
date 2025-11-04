import numpy as np
import matplotlib.pyplot as plt

def  f(x):
    return x**3 - 4 * x + 1

def bisection(f,a,b,tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    mid= b- f(b)*(a - b)/(f(a)-f(b))
    if abs(f(mid)) < tol:
        return mid
    if f(mid) * f(a) < 0:
        return bisection(f,a,mid,tol)
    else:
        return bisection(f,mid,b,tol)
    
    
root = bisection(f,-1,1)

n=np.arange(-10,10,0.2)

plt.plot(n,f(n),label='f(x) = x^3 - 4x + 1')
plt.scatter(root,f(root),color='red')
plt.axhline(root,color='blue',linestyle='--',label=f'Root at x={root:.5f}')

plt.axhline(0,color='black',linestyle='--')
plt.axvline(0,color='black',linestyle='--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method Root Finding')
plt.legend()
plt.grid()
plt.show()