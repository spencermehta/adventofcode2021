adjacentCoords = [(x,y) for x in range(-1,2) for y in range(-1,2) if not (x==0 and y==0)]

def getAdjacents(x, y, energies):
    adjacents = []
    for adjacent in adjacentCoords:
        newX = x + adjacent[0]
        newY =  y + adjacent[1]
        if newX >= 0 and newY >= 0 and newX < len(energies) and newY < len(energies[0]):
            adjacents.append((newX,newY))
    return adjacents


def increaseEnergies(energies):
    return [[(energy[0]+1, False) for energy in line]for line in energies]

def stepCell(x, y, energies):
    if not energies[x][y][1]:
        energies[x][y] = (energies[x][y][0] +1, energies[x][y][1])
        if energies[x][y][0] > 9:
            flash(x, y, energies)

def numFlashed(energies):
    count = 0
    for i in range(0, len(energies)):
        for j in range(0, len(energies[0])):
            if energies[i][j][1]:
                count += 1
    return count

flashes = 0

def flash(x, y, energies):
    global flashes
    if energies[x][y][0] > 9 and not energies[x][y][1]:
        energies[x][y] = (0, True)
        # print('flashing %s %s' % (x, y))
        flashes += 1
        for adj in getAdjacents(x, y, energies):
            stepCell(adj[0], adj[1], energies)

def step(energies):
    energies = increaseEnergies(energies)
    for i in range(0,len(energies)):
        for j in range(0, len(energies[0])):
            flash(i, j, energies)
    return energies



f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
energies = [ [(int(x), False) for x in line ]for line in lines]

i = 0
while (True):
    i+=1
    energies = step(energies)

    if numFlashed(energies) >= ( (len(energies)) * (len(energies[0]))):
        print(i)
        break

print(flashes)