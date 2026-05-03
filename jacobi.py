# Jacobi Iteration Method
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
    x_new = [0.0, 0.0, 0.0]
    for j in range(3):
        sum_ax = 0.0
        for k in range(3):
            if k != j:
                sum_ax += A[j][k] * x[k]
        x_new[j] = (b[j] - sum_ax) / A[j][j]
    
    print(f"{i+1:9} | {x_new[0]:.6f} | {x_new[1]:.6f} | {x_new[2]:.6f}")
    
    # Check convergence
    converged = True
    for j in range(3):
        if abs(x_new[j] - x[j]) > tol:
            converged = False
            break
    
    if converged:
        break
    
    x = x_new

print(f"\nFinal solution: x={x[0]:.6f}, y={x[1]:.6f}, z={x[2]:.6f}")
