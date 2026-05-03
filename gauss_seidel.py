# Gauss-Seidel Iteration Method
# Solve: 4x - y - z = 3, -2x + 6y + z = 9, -x + y + 7z = -6
# Initial guess: x=0, y=0, z=0, tolerance 0.001

# Coefficients
A = [
    [4, -1, -1],
    [-2, 6, 1],
    [-1, 1, 7]
]
b = [3, 9, -6]

x = [0.0, 0.0, 0.0]
tol = 0.001
max_iter = 100

print("Iteration | x       | y       | z")
print("-" * 35)

for i in range(max_iter):
    x_old = x[:]
    for j in range(3):
        sum_ax = 0.0
        for k in range(3):
            if k != j:
                sum_ax += A[j][k] * x[k]
        x[j] = (b[j] - sum_ax) / A[j][j]
    
    print(f"{i+1:9} | {x[0]:.6f} | {x[1]:.6f} | {x[2]:.6f}")
    
    # Check convergence
    converged = True
    for j in range(3):
        if abs(x[j] - x_old[j]) > tol:
            converged = False
            break
    
    if converged:
        break

print(f"\nFinal solution: x={x[0]:.6f}, y={x[1]:.6f}, z={x[2]:.6f}")
