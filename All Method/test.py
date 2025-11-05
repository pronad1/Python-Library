import numpy as np

def cramer(A,b):

    det_A=np.linalg.det(A)
    if det_A==0:
        print("Solution is not possible")
        return None
    
    n=len(b)
    z=np.zeros(n)
    for i in range(n):
        Ai=A.copy()
        Ai[:,i]=b
        z[i]=np.linalg.det(Ai)/det_A

    return z

A=np.array(eval(input("Enter the value of A as a list")),dtype=float)
b=np.array(eval(input("Enter the value of b as a list")),dtype=float)

solution = cramer(A,b)

print(solution)