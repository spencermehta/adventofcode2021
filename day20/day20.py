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
        c = coord(co[0], co[1], img)
        binNum += (img[c[1]][c[0]])
    binNum = ''.join(['0' if c == '.' else '1' for c in binNum])
    return algo[int(binNum, 2)]

def coord(x, y, img):
    midPt = (math.floor(len(img)/2), math.floor(len(img[0])/2))
    return (x+midPt[0], y+midPt[1])

def getOutputImg(img, algo):
    # print(len(img), len(img[0]))
    img = expandImg(img)
    img = expandImg(img)
    img = expandImg(img)

    # print('l', len(img), len(img[0]))
    # for row in img:
    #     print(row)
    startIndex = -(math.floor(len(img) /2 )-1)
    endIndex = math.floor(len(img) /2 )-1
    r = range(startIndex, endIndex)
    # print(r)
    # return [''.join([getOutputCell(j, i, img, algo) for j in r]) for i in r]
    return [''.join([getOutputCell(j, i, img, algo) for j in r])[1:] for i in r][1:]

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

img = getOutputImg(img, algo)
for row in img:
    print(row)
print('\n')

img = getOutputImg(img, algo)
for row in img:
    print(row)
print('\n')

# img = getOutputImg(img, algo)
# for row in img:
#     print(row)
# print('\n')
# img = getOutputImg(img, algo)
# for row in img:
#     print(row)
# print('\n')
# img = getOutputImg(img, algo)
# for row in img:
#     print(row)
# print('\n')
# img = getOutputImg(img, algo)
# for row in img:
#     print(row)
# print('\n')

print(litPixels(img))