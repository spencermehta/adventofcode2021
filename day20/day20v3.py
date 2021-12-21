import math

def getSurroundingCoords(x, y):
    return [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

def expandImg(img):
    img.insert(0, ''.join(['.' for i in range(0,len(img[0]))]))
    img.append(''.join(['.' for i in range(0,len(img[0]))]))
    img = ['.' + row + '.' for row in img]
    return img

def getOutputCell(x, y, img, algo):
    binNum = ''
    for co in getSurroundingCoords(x, y):
        if co[0] < 0 or co[1] < 0 or co[0] >= len(img) or co[1] >= len(img):
            binNum += '.'
        else:
            binNum += (img[co[1]][co[0]])
    binNum = ''.join(['0' if c == '.' else '1' for c in binNum])
    return algo[int(binNum, 2)]

def getOutputImg(img, algo):
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)

    # for row in img:
    #     print(row)

    startIndex = 3
    endIndex = len(img) -3
    r = range(startIndex, endIndex)
    return [''.join([getOutputCell(j, i, img, algo) for j in r]) for i in r]
    # return [''.join([getOutputCell(j, i, img, algo) for j in r])[1:-1] for i in r][1:-1]

def litPixels(img):
    return sum([row.count('#') for row in img])


f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))

algo = lines[0]
img = lines[2:]

# for row in img:
#     print(row)
# print('\n')

for i in range(0,1):
    img = getOutputImg(img, algo)

for row in img:
    print(row)
print('\n')

print(litPixels(img))