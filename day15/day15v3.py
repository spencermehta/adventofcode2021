def getNeighbours(xy):
    neighbours = [(xy[0]+1, xy[1]), (xy[0]-1, xy[1]), (xy[0], xy[1]+1),(xy[0],xy[1]-1)]
    if xy[0] == 0:
        neighbours.remove((xy[0]-1,xy[1]))
    if xy[1] == 0:
        neighbours.remove((xy[0],xy[1]-1))
    if xy[0] == len(grid)-1:
        neighbours.remove((xy[0]+1,xy[1]))
    if xy[1] == len(grid[0])-1:
        neighbours.remove((xy[0],xy[1]+1))
    return neighbours
    
def visit(node):
    visited.append(node)

f = open('myfile.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
grid = [[int(num) for num in line] for line in lines]

unvisited = dict()
for i in range(0,len(grid)):
    for j in range(0, len(grid[0])):
        unvisited[(i,j)] = 1000000000

costs = dict()
for i in range(0,len(grid)):
    for j in range(0, len(grid[0])):
        costs[(i,j)] = 1000000000

visited = []

costs[(0,0)] = 0



pos = (0,0)
while [len(grid)-1, len(grid[0])-1] not in visited:

    print('\t',len(unvisited), '\t\t', end='\r')
    curCost = costs[pos]
    neighbours = getNeighbours(pos)
    for neighbour in neighbours:
        c = curCost + grid[neighbour[0]][neighbour[1]]
        if c < costs[neighbour]:
            costs[neighbour] = c
            unvisited[neighbour] = c
    visited.append(pos)
    del unvisited[pos]

    if len(unvisited.keys()) == 0:
        break
    # print(sorted(unvisited.values())[:5])
    pos = min(unvisited, key=unvisited.get)

print(costs[(len(grid)-1,len(grid[0])-1)])