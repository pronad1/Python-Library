import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.2 +25 * x -200 * x**2 +675 * x**3 -900 * x**4 +400 * x**5

array=np.arange(-0.01,0.82,0.01)
plt.plot(array,f(array),label='fff')
plt.legend()
plt.show()

def trap(f,a,b):
    return (b-a)*(f(a)+f(b))/2

solution = trap(f,0,0.8)
print(solution)

plt.plot(array,f(array))
plt.plot([0,0.8],[f(0),f(0.8)],color='red',label='trap')
plt.legend()
plt.show()

def sim1(f,a,b):
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6


def sim3(f,a,b):
    h=(b-a)/3
    return (3*h/8)*(f(a)+3*f(h+a)+3*f(h+2*a)+f(b))


from scipy.interpolate import CubicSpline

a,b,c,d=0,0.8/3,2*0.8/3,0.8
print()