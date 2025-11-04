import numpy as np
import math

x=np.array(eval(input("Enter the values of x as a list: ")))
y=np.array(eval(input("Enter the values of y as a list: ")))
val=float(input("Enter the value of x to interpolate:"))

n=len(x)
h=x[1]-x[0]
u=(val-x[0])/h

diff=np.zeros((n,n))
diff[:,0]=y
for i in range(1,n):
    for j in range(n-i):
        diff[j,i]=diff[j+1,i-1]-diff[j,i-1]

result=y[0]
u_term=1
for i in range(1,n):
    u_term*=(u-(i-1))
    result+=diff[0,i]*u_term/math.factorial(i)

print("The interpolated value at x =", val, "is", result)

u=(val - x[-1])/h
diff=np.zeros((n,n))
diff[:,0]=y
for i in range(1,n):
    for j in range(i,n):
        diff[j,i]=diff[j,i-1]-diff[j-1,i-1]

result=y[-1]
u_term=1
for i in range(1,n):
    u_term*=(u+(i-1))
    result+=diff[n-1,i]*u_term/math.factorial(i)

print("The interpolated value at x =", val, "using backward difference is", result) 