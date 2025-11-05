import numpy as np
import math

x=np.array(eval(input()),dtype=float)
y=np.array(eval(input()),dtype=float)

val=float(input())

h=x[1]-x[0]
u=(val-x[-1])/h

n=len(x)
diff=np.zeros((n,n))
diff[:,0]=y
for i in range(1,n):
    for j in range(i,n):
        diff[j,i]=diff[j,i-1] - diff[j-1,i-1]

u_term=1
result=y[-1]

for  i in range(1,n):
    u_term*=(u+(i-1))
    result += (diff[-1,i]*u_term)/math.factorial(i)

print(result)