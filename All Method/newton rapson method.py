import math

def f(t):
    return 5000*(1.05**t) - 10000

def f_prime(t):
    return 5000*(1.05**t)*math.log(1.05)

def newton_raphson(t0, tol=1e-6, max_iter=100):
    print("Iter |   t")
    print("-----------------")
    for i in range(max_iter):
        t1 = t0 - f(t0)/f_prime(t0)
        print(f"{i+1:3d}  | {t1:.6f}")
        if abs(t1 - t0) < tol:
            print("\nConverged in", i+1, "iterations.")
            return t1
        t0 = t1
    print("\nDid not converge within max iterations.")
    return None

t0 = 5
solution = newton_raphson(t0)
print("\nApproximate time to double investment =", round(solution, 2), "years")
