def getNeighbours(xy):
    neighbours = [[xy[0]+1, xy[1]], [xy[0]-1, xy[1]], [xy[0], xy[1]+1],[xy[0],xy[1]-1]]
    if xy[0] == 0:
        neighbours.remove([xy[0]-1,xy[1]])
    if xy[1] == 0:
        neighbours.remove([xy[0],xy[1]-1])
    if xy[0] == len(grid)-1:
        neighbours.remove([xy[0]+1,xy[1]])
    if xy[1] == len(grid[0])-1:
        neighbours.remove([xy[0],xy[1]+1])
    return neighbours
    
def visit(node):
    visited.append(node)

f = open('testlargeinput.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
grid = [[int(num) for num in line] for line in lines]

cost = [[100000000 for col in range(0,len(grid[0]))] for row in range(0,len(grid))]
prev =  [[None for col in range(0,len(grid[0]))] for row in range(0,len(grid))]
visited = []

cost[0][0] = 0



pos = [0,0]
while [len(grid)-1, len(grid[0])-1] not in visited:
    # input()
    print(pos, len(visited))
    curCost = cost[pos[0]][pos[1]]
    # print('curCost', curCost)
    neighbours = getNeighbours(pos)
    # print('neighbours', neighbours)
    for neighbour in neighbours:
        c = curCost + grid[neighbour[0]][neighbour[1]]
        # print(neighbour, c)
        if c < cost[neighbour[0]][neighbour[1]]:
            # print('reducing cost of', neighbour, 'from', cost[neighbour[0]][neighbour[1]], 'to', c)
            cost[neighbour[0]][neighbour[1]] = c
            prev[neighbour[0]][neighbour[1]] = pos
    visited.append(pos)
    # print('visited is now', visited)
    unvisitedCosts = [cost[ix][iy] for ix, row in enumerate(cost) for iy, i in enumerate(row) if [iy, ix] not in visited]
    unvisitedCoords = [[ix, iy] for ix, row in enumerate(cost) for iy, i in enumerate(row) if [iy, ix] not in visited]
    minUnvisitedCosts = min(unvisitedCosts)
    # print('minUnvisC', minUnvisitedCosts)
    coordsOfMinUnvisitedCost = [coord for coord in unvisitedCoords if coord not in visited]
    if len(coordsOfMinUnvisitedCost) == 0:
        break
    pos = coordsOfMinUnvisitedCost[0]
print(cost[len(grid)-1][len(grid[0])-1])