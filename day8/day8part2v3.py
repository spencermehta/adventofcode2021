f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lines = list(map(lambda x: x.split("|"), lines))
lines = list(map(lambda xs: [xs[0].split(), xs[1].split()], lines))

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

def isThree(one, num):
    print(one, num)
    if len(num) != 5:
        return False
    return one[0] in num and one[1] in num

def isNine(three, num):
    print(three, num)
    if len(num) != 6:
        return False
    return three[0] in num and three[1] in num and three[2] in num and three[3] in num and three[4] in num

def isZero(eight, one, num):
    if len(num) != 6:
        return False
    return num[0] in eight and num[1] in eight and num[2] in eight and num[3] in eight and num[4] in eight and num[5] in eight and one[0] in num and one[1] in num
    
def isFive(six, num):
    if len(num) != 5:
        return False
    count = 0
    for i in range(0,5):
        if num[i] in six:
            count+= 1
    return count == 5

def decode(line):
    data = findUniques(line)
    del line[line.index(data[1])]
    del line[line.index(data[4])]
    del line[line.index(data[7])]
    del line[line.index(data[8])]
    for num in line:
        if isThree(data[1], num):
            data[3] = num
            del line[line.index(num)]
    for num in line:
        if isNine(data[3], num):
            data[9] = num
            del line[line.index(num)]
    for num in line:
        if isZero(data[8], data[1], num):
            data[0] = num
            del line[line.index(num)]
    for num in line:
        if len(num) == 6:
            data[6] = num
            del line[line.index(num)]
    for num in line:
        if isFive(data[6], num):
            data[5] = num
            del line[line.index(num)]
    data[2] = line[0]

    

    return data

def decodeNum(num, data):
    data =list(map(lambda x: ''.join(sorted(x)), data))
    print(data)
    sortedNum = ''.join(sorted(num))
    print(sortedNum)
    return data.index(sortedNum)

def parseLine(line):
    data = decode(line[0])
    print(line, data)
    nums = int(''.join(map(lambda x: str(x),list(map(lambda x: decodeNum(x, data), line[1])))))
    return nums

print(sum(list(map(parseLine, lines))))