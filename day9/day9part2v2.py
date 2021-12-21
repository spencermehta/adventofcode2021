from functools import reduce

def getAdjacents(x, y, mat):
    adjacents = []

    if x+1 < len(mat):
        adjacents.append((x+1, y))
    if x-1>= 0:
        adjacents.append((x-1, y))
    if y+1 < len(mat[0]):
        adjacents.append((x, y+1))
    if y-1 >= 0:
        adjacents.append((x, y-1))
    return adjacents

def isLowerThanAdjacents(v, adjacents, mat):
    return all(mat[i[0]][i[1]] > v for i in adjacents)
    
def riskLevel(x, y, lines):
    return lines[x][y] + 1

def isInBasin(p, adjacents, basin, mat):
    # if mat[p[0]][p[1]] == 9:
    #     return False
    isBasin =  all(mat[i[0]][i[1]] > mat[p[0]][p[1]] for i in adjacents if i not in basin)
    # print(p, isBasin, mat[p[0]][p[1]])
    return isBasin

def constructBasin(lowPoint, mat, basin):
    if lowPoint in basin:
        return basin
    if mat[lowPoint[0]][lowPoint[1]] == 9:
        return basin
    basin.append(lowPoint)
    adjs = getAdjacents(lowPoint[0], lowPoint[1], mat)
    for adj in adjs:
        if isInBasin(adj, getAdjacents(adj[0], adj[1], mat), basin, mat):
            basin = constructBasin(adj, mat, basin)
    return basin


f = open('input2.txt')
lines = f.readlines()
lines = list(map(lambda x: list(x.strip('\n')), lines))
lines = [[int(l) for l in line] for line in lines]

lowPoints = []
basins = []

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if isLowerThanAdjacents(lines[i][j], getAdjacents(i, j, lines), lines):
            lowPoints.append((i,j))
print(sum(list(map(lambda xy: riskLevel(xy[0], xy[1], lines), lowPoints))))

print(len(lowPoints))
# print(constructBasin((2,2), lines, []))
basins = []
for lowPoint in lowPoints:
    basins.append(len(constructBasin(lowPoint, lines, [])))

print(len(basins))
# print(sorted(basins))
topthree = sorted(basins)[-3:]
print(topthree)
print(reduce(lambda x, y: x*y, topthree))