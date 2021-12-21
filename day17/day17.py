def xArithmeticProg(x,n):
    a = x
    d = -1
    sn = n/2 * (2*a + (n-1)*d)
    return int(sn)
     
def canBeX(x, xTarget, minX):
    return any([xArithmeticProg(x, n) >= xTarget[0] and xArithmeticProg(x, n) <= xTarget[1] for n in range(1,minX)])

def possibleNumSteps(xTarget):
    maxX = xTarget[1]
    triNums = getTriNumsUpTo(maxX)
    diff = set(triNums).intersection(set([i for i in range(xTarget[0], xTarget[1]+1)]))
    minX = triNums.index(min(diff))
    poss = [i for i in range(minX, maxX+1)]
    # return [i for i in poss if canBeX(i, xTarget, minX)]

    possibles = dict()
    for x in poss:
        ns = [n for n in range(1,minX) if xArithmeticProg(x, n) >= xTarget[0] and xArithmeticProg(x, n) <= xTarget[1]]
        if len(ns) > 0:
            possibles[x] = ns
    return possibles

def getTriNumsUpTo(maxTriNum):
    triNums = [0]
    i=1
    n=0
    while n <= maxTriNum:
        n = triNums[i-1] + i
        triNums.append(n)
        i+=1
    return triNums



f = open('testinput.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
target = lines[0].replace(' ', '')
target = target.split(':')[1].split(',')
target = [t.split('=')[1] for t in target]
target = [list(map(int, t.split('..'))) for t in target]
print(target)

possibleXs = possibleNumSteps(target[0])

minY = target[1][0]
steps = list(possibleXs.values())
maxSteps = max([item for sublist in steps for item in sublist])

possibles = []
for x in possibleXs.keys():
    for n in possibleXs[x]:
        print(x, n)
        for y in range(0,10):
            sn = xArithmeticProg(y, n)
            print(f"\t{y}: {sn}")
            if sn <= target[1][1] and sn >= target[1][0]:
                possibles.append((x,y,n))
print(possibles)



