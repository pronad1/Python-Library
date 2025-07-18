import matplotlib.pyplot as plt
import numpy as np

# f(x)=x^2
x=np.linspace(-5,5,100)
plt.plot(x,x**2,'g--')
plt.show()

# f(x)=x^2 and f(x)=x^3
x=np.linspace(-5,5,20)
plt.plot(x,x**2,'ko')
plt.plot(x,x**3,'r*')
plt.show()

x=[3.58,3.41,3.84,3.87]
plt.plot(x)
plt.show()
