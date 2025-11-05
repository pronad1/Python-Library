import numpy as np

A=np.array(eval(input()),dtype=float)
b=np.array(eval(input()),dtype=float)

n=len(b)
x=np.zeros(n)

for i in range(n):
    privot=A[i,i]
    A[i]=A[i]/privot
    b[i]=b[i]/privot
    for j in range(n):
        factor=A[j,i]
        if j!=i:
            A[j]-=factor*A[i]
            b[j]-=factor*b[i]



print(A)

print()

print(b)