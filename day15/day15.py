
f = open('myfile.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
grid = [[int(num) for num in line] for line in lines]

costs = [[-0 for col in range(0,len(grid[0]))] for row in range(0,len(grid))]
costs[0][0] = 0
for i in range(1,len(grid)):
    costs[i][0] = grid[i][0] + costs[i-1][0]
for i in range(1,len(grid[0])):
    costs[0][i] = grid[0][i] + costs[0][i-1]

for x in range(1, len(grid)):
    for y in range(1, len(grid[0])):
        costs[x][y] = min(costs[x-1][y], costs[x][y-1]) + grid[x][y]

print(costs[len(grid)-1][len(grid[0])-1])
print(len(grid), len(grid[0]))

# for row in grid:
#     print(row)

# for row in costs:
#     for col in row:
#         print(col, end="\t")
#     print()