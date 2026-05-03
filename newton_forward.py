# Newton Forward Interpolation
# Data: x = [0,1,2,3], y = [1,2,4,8], interpolate at x=1.5

x = [0, 1, 2, 3]
y = [1, 2, 4, 8]
xp = 1.5

# Calculate forward differences
n = len(x)
diff = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    diff[i][0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

# Find h and p
h = x[1] - x[0]
p = (xp - x[0]) / h

# Interpolate
yp = diff[0][0]
term = 1
for i in range(1, n):
    term *= (p - (i-1)) / i
    yp += term * diff[0][i]

print(f"Interpolated value at x={xp} is {yp:.6f}")
