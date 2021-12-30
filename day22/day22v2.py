import math

def getLenInDims(instr):
    xs = instr[1]
    ys = instr[2]
    zs = instr[3]

    return xs[1]+1 - xs[0], ys[1]+1 - ys[0], zs[1]+1 - zs[0]
    # return abs(xs[1]+1 - xs[0]), abs(ys[1]+1 - ys[0]), abs(zs[1]+1 - zs[0])

def getNumSwitched(lens):
    return lens[0] * lens[1] * lens[2]

def getOverlapDimension(instr, prevInstr, dim):
    xs = instr[dim]
    pxs = prevInstr[dim]

    return [max(xs[0], pxs[0]), min(xs[1], pxs[1])]

    # overlap = 0
    # if pxs[0] > xs[0]:
    #     if pxs[1] < xs[1]:
    #         overlap = [pxs[0], pxs[1]]
    #     else:
    #         overlap = [pxs[0], xs[1]]
    # elif pxs[1] < xs[1]:
    #     overlap = [xs[0], pxs[1]]
    # else:
    #     overlap = []
    # return overlap

def getOverlap(instr, prevInstr):
    x = getOverlapDimension(instr, prevInstr, 1)
    y = getOverlapDimension(instr, prevInstr, 2)
    z = getOverlapDimension(instr, prevInstr, 3)

    sign = 1
    if instr[0] == prevInstr[0]:
        sign = -instr[0]
    
    elif instr[0] == -1 and prevInstr[0] == 1:
        sign = -1

    return [sign,x,y,z]

def doesOverlap(instr, prevInstr):
    if not(instr[1][0] <= prevInstr[1][1] and instr[1][1] >= prevInstr[1][0]):
        return False

    if not(instr[2][0] <= prevInstr[2][1] and instr[2][1] >= prevInstr[2][0]):
        return False

    if not(instr[3][0] <= prevInstr[3][1] and instr[3][1] >= prevInstr[3][0]):
        return False

    return True



# def getNewSwitches(instr, prevInstr):
#     return getNumSwitched(getLenInDims(instr)) - getNumSwitched(getLenInDims(getOverlap(instr, prevInstr)))

f = open('input.txt')
lines = f.readlines()
instrs = list(map(lambda x: x.strip('\n').split(' ') , lines))
instrs = list(map(lambda instr: list(map(lambda x:x.split(','), instr)), instrs))
instrs = [[*instr[0],  list(map(lambda x: x.split('=')[1].split('..'), instr[1]))] for instr in instrs]
instrs = [[1 if instr[0] == 'on' else -1, *list(map(lambda x: list(map(int, x)), instr[1]))] for instr in instrs]

prevInstrs = []
for instr in instrs:
    # if instr[1][0] >= -50 and instr[1][1] <= 50 and instr[2][0] >= -50 and instr[2][1] <= 50 and instr[3][0] >= -50 and instr[3][1] <= 50: 
    # print('instr:', instr)
    overlaps = []
    for prevInstr in prevInstrs:
        if doesOverlap(instr, prevInstr):
            overlap = getOverlap(instr, prevInstr)
            # print('overlaps with', prevInstr, getNumSwitched(getLenInDims(overlap)))
            overlaps.append(overlap)
    
    for overlap in overlaps:
        prevInstrs.append(overlap)
    # print('overlaps: ',len(overlaps))
    
    if instr[0] == 1:
        prevInstrs.append(instr)

    # total = 0
    # for instr in prevInstrs:
        # total += getNumSwitched(getLenInDims(instr)) * instr[0]
    # print('current total:', total, '\n')

total = 0
for instr in prevInstrs:
    total += getNumSwitched(getLenInDims(instr)) * instr[0]

print(total)