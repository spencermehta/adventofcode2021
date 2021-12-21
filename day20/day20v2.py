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
        binNum += (img[co[1]][co[0]])
    binNum = ''.join(['0' if c == '.' else '1' for c in binNum])
    return algo[int(binNum, 2)]

def getOutputImg(img, algo):
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)

    startIndex = 1
    endIndex = len(img) -1
    r = range(startIndex, endIndex)
    return [''.join([getOutputCell(j, i, img, algo) for j in r]) for i in r]
    # return [''.join([getOutputCell(j, i, img, algo) for j in r])[1:] for i in r][1:]

def litPixels(img):
    return sum([row.count('#') for row in img])


f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))

algo = lines[0]
img = lines[2:]


# print(getOutputCell(0,0, img, algo))
for row in img:
    print(row)
print('\n')

for i in range(0,3):
    print(i)
    img = getOutputImg(img, algo)

for row in img:
    print(row)
print('\n')

# cImg = [r[25:-25] for r in img][25:-25]
# for row in cImg:
#     print(row)
# print(litPixels(cImg))