
grid = [[0 for _ in range(16)] for _ in range(16)]

for i in range(16):
    grid[0][i] = 1
    grid[i][0] = 1

for i in range(1, 16):
    for j in range(1, 16):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[15][15])
