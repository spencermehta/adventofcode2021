import copy

class Point:
    def __init__(self, newX,newY):
        self.x = newX
        self.y = newY
    
    def __repr__(self):
        return ('Point (' + str(self.x) + ',' + str(self.y) + ')')

    def __str__(self):
        return ('Point (' + str(self.x) + ',' + str(self.y) + ')')

    def __eq__(self, other):
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False

class Line:
    def __init__(self, newStart, newEnd):
        self.start = newStart
        self.end = newEnd
    
    def __repr__(self):
        return "Line (%s -> %s)" % (self.start, self.end)

def parseLine(line):
    points = map(lambda x: x.split(','), line)
    intCoords = [[int(coord) for coord in point]for point in points]
    newPoints = map(lambda xy: Point(xy[0], xy[1]), intCoords)
    return Line(newPoints[0], newPoints[1])

def isNotDiagonal(line):
    return line.start.x == line.end.x or line.start.y == line.end.y

def getCoveringPoints(line):
    if not isNotDiagonal(line):
        return []
    points = []
    currPos = copy.deepcopy(line.start)
    points.append(copy.deepcopy(currPos))
    while currPos.x != line.end.x:
        currPos.x = currPos.x + 1 if line.end.x > currPos.x else currPos.x - 1
        points.append(copy.deepcopy(currPos))
    while currPos.y != line.end.y:
        currPos.y = currPos.y + 1 if line.end.y > currPos.y else currPos.y - 1
        points.append(copy.deepcopy(currPos))
    return points

def plotCoveringPointsOnGrid(lineCoveringPoints, grid):
    for point in lineCoveringPoints:
        grid[point.x][point.y] += 1

def flatten(board):
    return [item for row in board for item in row]


f = open('input.txt')
lines = f.readlines()
lines = map(lambda x: x.strip('\n'), lines)
lines = map(lambda x: x.split(' -> '), lines)
lines = map(parseLine, lines)
coveringPoints = map(getCoveringPoints, lines)

grid = [[0 for column in range(0,1000)] for row in range(0,1000)]
map(lambda x: plotCoveringPointsOnGrid(x, grid), coveringPoints)

flatGrid = flatten(grid)
print(len([point for point in flatGrid if point >= 2]))