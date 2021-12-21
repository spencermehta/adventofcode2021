def foldX(xy, x):
    if xy[0] > x:
        rem = (xy[0] % x)
        if rem == 0:
            xy[0] = 0
        else: xy[0] = x - rem
    return xy

def foldY(xy, y):
    if xy[1] > y:
        rem = (xy[1] % y)
        if rem == 0:
            xy[1] = 0
        else: xy[1] = y - rem
    return xy

def fold(xy, fold):
    if fold[0] == 'x':
        return foldX(xy, fold[1])
    else:
        return foldY(xy, fold[1])

def countGrid(grid):
    return sum([sum(row) for row in grid])


f = open('gavin3.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))

folds = [e for e in lines if e[0:4] == "fold"]

coords = [e for e in lines if e not in folds and e != '']
coords = [e.split(',') for e in coords]
coords = [[int(c) for c in e] for e in coords]

folds = [fold.strip('fold along ') for fold in folds]
folds = [fold.split('=') for fold in folds]
folds = [[x, int(y)] for [x,y] in folds]


for singleFold in folds:
    coords = [fold(coord, singleFold) for coord in coords]

# print(coords)

xs = [xy[0] for xy in coords]
maxX = max(xs)
ys = [xy[1] for xy in coords]
maxY = max(ys)

grid = [[0 for x in range(0,maxX + 1)] for y in range(0,maxY + 1)]

for xy in coords:
    grid[xy[1]][xy[0]] = '#'

print('\n\n')
for row in grid:
    for c in row:
        if c == '#':
            print('\033[95m%s' % c, end='')
        else:
            print(' ', end='')
    print('')
print('\n\n')

# print(countGrid(grid))