import math

def executeStep(instr, grid):
    xs = instr[1]
    ys = instr[2]
    zs = instr[3]
    gridSet = True if instr[0] == 'on' else False

    coords = [(x,y,z) for z in range(zs[0], zs[1]+1) for y in range(ys[0], ys[1]+1) for x in range(xs[0], xs[1]+1)]
    for coord in coords:
        c = mapCoord(coord, grid)
        if (c[0] < len(grid)) and (c[1] < len(grid[0])) and (c[2] < len(grid[0][0])):
            grid[c[0]][c[1]][c[2]] = gridSet
    return grid
            

def mapCoord(coord, grid):

    x = math.floor(len(grid)/2) + coord[0]
    y = math.floor(len(grid[0])/2) + coord[1]
    z = math.floor(len(grid[0][0])/2) + coord[2]
    return (x,y,z)

def countGrid(grid):
    return sum([sum([sum([y.count(True)]) for y in x]) for x in grid])

f = open('testinput2.txt')
lines = f.readlines()
instrs = list(map(lambda x: x.strip('\n').split(' ') , lines))
instrs = list(map(lambda instr: list(map(lambda x:x.split(','), instr)), instrs))
instrs = [[*instr[0],  list(map(lambda x: x.split('=')[1].split('..'), instr[1]))] for instr in instrs]
instrs = [[instr[0], *list(map(lambda x: list(map(int, x)), instr[1]))] for instr in instrs]
# instrs = [[i if i == 'on' or i == 'off' else list(map(int, i.split('=')[1].split('..'))) for i in instr] for instr in instrs]
print(instrs)

grid = [[[ False for k in range(0,100)]for j in range(0,100)] for i in range(0,100)]
# print(grid)

# print(mapCoord((0,0,0), grid))
for instr in instrs:
    # if instr[1][0] >= -50 and instr[1][1] <= 50 and instr[2][0] >= -50 and instr[2][1] <= 50 and instr[3][0] >= -50 and instr[3][1] <= 50: 
    grid = executeStep(instr, grid)
print(countGrid(grid))
