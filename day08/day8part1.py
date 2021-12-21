import functools

def getCountOfNumSegments(numSegments, line):
    return functools.reduce(lambda x, y: x+1 if len(y) == numSegments else x, line[1], 0)

def getCountOfNumSegmentsList(numSegmentsList, line):
    return list(map(lambda x: getCountOfNumSegments(x, line), numSegmentsList))

def sumLists(lists):
    return sum(list(map(sum, lists)))

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lines = list(map(lambda x: x.split("|"), lines))
lines = list(map(lambda xs: [xs[0].split(), xs[1].split()], lines))

uniqueSegments = [2,3,4,7]
print(lines[0])
print(getCountOfNumSegments(2, lines[0]))
print(sumLists(list(map(lambda line: getCountOfNumSegmentsList(uniqueSegments, line), lines))))