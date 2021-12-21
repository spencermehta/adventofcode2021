
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

def isInBasin(basin, x, y, adjacents, mat, lowPoints):
    print(x,y, lowPoints)
    if (x,y) in lowPoints:
        return True

    # print(adjacents)
    print(mat[x][y])

    for i in adjacents:
        print(i)
        print(mat[i[0]][i[1]])
    if all(mat[i[0]][i[1]] > mat[x][y] for i in adjacents if i not in lowPoints and i not in basin):  
        return True
    # elif (x,y) in lowPoints:
    #     return True
    # else:
    #     return False
    
def riskLevel(x, y, lines):
    return lines[x][y] + 1

f = open('testinput.txt')
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
print(isInBasin([(0,1)], 1,0, getAdjacents(1,0, lines), lines, lowPoints))