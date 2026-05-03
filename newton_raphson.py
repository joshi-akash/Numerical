# Newton-Raphson Method
# Solve f(x) = x^2 - 4 = 0 with initial guess x0 = 3, tolerance 0.001

def f(x):
    return x**2 - 4

def df(x):
    return 2 * x

x0 = 3.0
tol = 0.001
max_iter = 100

print("Iteration | x       | f(x)    | f'(x)   | Error")
print("-" * 50)

for i in range(max_iter):
    fx = f(x0)
    dfx = df(x0)
    x1 = x0 - fx / dfx
    error = abs(x1 - x0)
    
    print(f"{i+1:9} | {x0:.6f} | {fx:.6f} | {dfx:.6f} | {error:.6f}")
    
    if error < tol:
        break
    
    x0 = x1

print(f"\nRoot found: {x1:.6f}")
