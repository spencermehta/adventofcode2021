import functools
import copy

def getCountOfNumSegments(numSegments, line):
    return functools.reduce(lambda x, y: x+1 if len(y) == numSegments else x, line[1], 0)

def getCountOfNumSegmentsList(numSegmentsList, line):
    return list(map(lambda x: getCountOfNumSegments(x, line), numSegmentsList))

def sumLists(lists):
    return sum(list(map(sum, lists)))

def commonElements(listA, listB):
    return list(set(listA).intersection(listB))

def difference(listA, listB):
    return list(set(listA).difference(listB))

def listEquals(listA, listB):
    return difference(listA,listB) == [] and difference(listB, listA) == []

def findUniques(numbers):
    data = ['' for i in range(0,10)]
    [one] = [num for num in numbers if len(num)== 2]
    data[1] = one

    [four] = [num for num in numbers if len(num) == 4]
    data[4] = four

    [seven] = [num for num in numbers if len(num) == 3]
    data[7] = seven

    [eight] = [num for num in numbers if len(num) == 7]
    data[8] = eight
    return data

def findThree(numbers, data):
    [three] = [num for num in numbers if listEquals(commonElements(data[1], num), list(data[1])) and len(num) == 5]
    data[3] = three

def findSix(numbers, data, encoding):
    [six] = [num for num in numbers if len(num) == 6 and encoding[3][0] in num and encoding[4][0] in num]
    data[6] = six


def determineA(data, encoding):
    encoding[0] =  difference(data[7], data[1])


def determineCF(data, encoding):
    common = commonElements(data[1], data[7])
    encoding[2] = common
    encoding[5] = common

def determineBD(data, encoding):
    diff = difference(data[4], data[1])
    encoding[1] = diff
    encoding[3] = diff

def determineEG(data, encoding):
    diff = difference(data[8], data[4])
    diff2 = difference(diff, encoding[0])
    encoding[4] = diff2
    encoding[6] = diff2

def determineB(data, encoding):
    diff = difference(data[4], data[3])
    encoding[1] = diff

def determineG(data, encoding):
    diff = difference(data[3], data[4])
    diff2 = difference(diff, encoding[0])
    encoding[6] = diff2

def determineD(data, encoding):
    diff = difference(data[4], data[1])
    diff2 = difference(diff, encoding[1])
    encoding[3] = diff2

def determineE(data, encoding):
    diff = difference(data[8], data[3])
    diff2 = difference(diff, encoding[1])
    encoding[4] = diff2

def determineC(data, encoding):
    diff = difference(data[8], data[6])
    diff2 = difference(encoding[2], diff)
    encoding[2] = diff
    encoding[5] = diff2

def getEncoding(line):
    encoding = [['a','b','c','d','e','f','g'] for i in range(0,7)]
    data = findUniques(line)
    determineA(data, encoding)
    determineCF(data, encoding)
    determineBD(data, encoding)
    determineEG(data, encoding)
    findThree(line, data)
    determineB(data, encoding)
    determineG(data, encoding)
    determineD(data, encoding)
    determineE(data, encoding)
    findSix(line, data, encoding)
    determineC(data, encoding)

    return encoding

def getChar(char, encoding):
    for i in range(0, len(encoding)):
        if encoding[i] == [char]:
            return characters[i]

def decode(encoding, digit):
    decoding = ''
    for char in digit:
        decoding += getChar(char, encoding)
    return decoding

def decodeNum(encoding, num):
    decoding = decode(encoding, num)
    decoding = ''.join(sorted(decoding))
    return unencoded.index(decoding)

def decodeLine(encoding, line):
    return int(''.join(map(lambda x: str(x), list(map(lambda x: decodeNum(encoding, x), line)))))

def decodeLines(encoding, lines):
    return list(map(lambda x: decodeLines(encoding,x[1]), lines))

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lines = list(map(lambda x: x.split("|"), lines))
lines = list(map(lambda xs: [xs[0].split(), xs[1].split()], lines))

unencoded = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
characters = ['a','b','c','d','e','f','g']

encoding = getEncoding(lines[0][0])

for line in lines:
    print(decodeLine(encoding, line[1]))
