
def getAdjacents(x, y, mat):
    adjacents = []

    if x+1 < len(mat):
        adjacents.append(mat[x+1][y])
    if x-1>= 0:
        adjacents.append(mat[x-1][y])
    if y+1 < len(mat[0]):
        adjacents.append(mat[x][y+1])
    if y-1 >= 0:
        adjacents.append(mat[x][y-1])
    return adjacents

def isLowerThanAdjacents(v, adjacents):
    return all(i > v for i in adjacents)
    
def riskLevel(x, y, lines):
    return lines[x][y] + 1

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: list(x.strip('\n')), lines))
lines = [[int(l) for l in line] for line in lines]
print(lines)

print(isLowerThanAdjacents(1, getAdjacents(0,0,lines)))

lowPoints = []

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if isLowerThanAdjacents(lines[i][j], getAdjacents(i, j, lines)):
            lowPoints.append((i,j))
print(sum(list(map(lambda xy: riskLevel(xy[0], xy[1], lines), lowPoints))))
