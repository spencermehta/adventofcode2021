import math
f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
oldgrid = [[int(num) for num in line] for line in lines]

lenX = len(oldgrid)
lenY = len(oldgrid[0])
print(lenX, lenY)

# grid = [[(oldgrid[i % lenX][j % lenX] -1 + i +j) % 9 + 1 for j in range(0,len(oldgrid[0])*5)] for i in range(0,len(oldgrid)*5)]
grid = [[(oldgrid[i % lenX][j % lenX] -1 + math.floor(i/lenX) +math.floor(j/lenX)) % 9 +1 for j in range(0,len(oldgrid[0])*5)] for i in range(0,len(oldgrid)*5)]

# strgrid = [''.join(l) for l in grid]
# print(strgrid)

f = open("myfile.txt", "a")
strgrid =[''.join(map(str, l)) for l in grid]
for l in strgrid:
    f.write(l + '\n')
f.close()

# for row in grid:
#     print(row)

# print(len(grid), len(grid[0]))

# costs = [[-0 for col in range(0,len(grid[0]))] for row in range(0,len(grid))]
# costs[0][0] = 0
# for i in range(1,len(grid)):
#     costs[i][0] = grid[i][0] + costs[i-1][0]
# for i in range(1,len(grid[0])):
#     costs[0][i] = grid[0][i] + costs[0][i-1]

# for x in range(1, len(grid)):
#     for y in range(1, len(grid[0])):
#         costs[x][y] = min(costs[x-1][y], costs[x][y-1]) + grid[x][y]

# for row in costs:
#     print(row[0])

# for i in range(0,5):
#     for j in range(0,5):
#         print(grid[99 + i*lenX][99 + j*lenX], end="\t")
#     print()
# print(costs[len(grid)-1][len(grid[0])-1])