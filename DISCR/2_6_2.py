n = 16
grid = [[0 for _ in range(n)] for _ in range(n)]

grid[0][1] = 1
grid[1][0] = 1

for i in range(1, n):
    for j in range(1, n):
        if i == j and i + 1 < n:
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            grid[i + 1][j] = grid[i][j] - grid[i - 1][j]
        if i == j and i + 1 >= n:
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            break
        elif j - i == 1:
            grid[i][j] = grid[i][j - 1]
    if i + 1 >= n:
        break

print(grid[n - 1][n - 1])