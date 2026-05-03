# Regula Falsi Method
# Solve f(x) = x^2 - 4 = 0 in interval [1, 3] with tolerance 0.001

def f(x):
    return x**2 - 4

a = 1.0
b = 3.0
tol = 0.001
max_iter = 100

print("Iteration | a       | b       | c       | f(c)    | Error")
print("-" * 60)

for i in range(max_iter):
    fa = f(a)
    fb = f(b)
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)
    error = abs(b - a)
    
    print(f"{i+1:9} | {a:.6f} | {b:.6f} | {c:.6f} | {fc:.6f} | {error:.6f}")
    
    if abs(fc) < tol or error < tol:
        break
    
    if fa * fc < 0:
        b = c
    else:
        a = c

print(f"\nRoot found: {c:.6f}")
