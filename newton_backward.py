# Newton Backward Interpolation
# Data: x = [0,1,2,3], y = [1,2,4,8], interpolate at x=2.5

x = [0, 1, 2, 3]
y = [1, 2, 4, 8]
xp = 2.5

# Calculate backward differences
n = len(x)
diff = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    diff[i][0] = y[i]

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

# Find h and p
h = x[1] - x[0]
p = (xp - x[n-1]) / h

# Interpolate
yp = diff[n-1][0]
term = 1
for i in range(1, n):
    term *= (p + (i-1)) / i
    yp += term * diff[n-1][i]

print(f"Interpolated value at x={xp} is {yp:.6f}")
