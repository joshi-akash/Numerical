# Gauss Elimination Method
# Solve system: 2x + y - z = 8, -3x - y + 2z = -11, -2x + y + 2z = -3

# Augmented matrix [A|b]
matrix = [
    [2.0, 1.0, -1.0, 8.0],
    [-3.0, -1.0, 2.0, -11.0],
    [-2.0, 1.0, 2.0, -3.0]
]

n = len(matrix)

# Forward elimination
for i in range(n):
    # Make diagonal element 1
    pivot = matrix[i][i]
    for j in range(i, n+1):
        matrix[i][j] /= pivot
    
    # Eliminate below
    for k in range(i+1, n):
        factor = matrix[k][i]
        for j in range(i, n+1):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution
x = [0.0] * n
for i in range(n-1, -1, -1):
    x[i] = matrix[i][n]
    for j in range(i+1, n):
        x[i] -= matrix[i][j] * x[j]

print("Solution:")
print(f"x = {x[0]:.6f}")
print(f"y = {x[1]:.6f}")
print(f"z = {x[2]:.6f}")
