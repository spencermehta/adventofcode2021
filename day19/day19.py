class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def translate(self, c, t):
        if c == 'x':
            return Point(self.x + t, self.y, self.z)
        elif c == 'y':    
            return Point(self.x, self.y + t, self.z)
        elif c == 'z':    
            return Point(self.x, self.y, self.z + t)

    def translateX(self, x):
        return Point(self.x + x, self.y, self.z)

    def translateY(self, y):
        return Point(self.x, self.y + y, self.z)

# def compareScanners(scannerA, scannerB, attr):
#     A = sorted([getattr(p, attr) for p in scannerA])
#     B = sorted([getattr(p, attr) for p in scannerB])

#     curTranslationAIndex = -12
#     numInter = 0
#     while numInter < 12 and curTranslationAIndex < 11:
#         curTranslationAIndex += 1
#         translation = A[curTranslationAIndex] - B[11]
#         newScannerB = map(lambda p: p.translate(attr, translation), scannerB)
#         newB = sorted([getattr(p, attr) for p in newScannerB])
#         numInter = len(set(newB).intersection(A))
#         if numInter >= 12:
#             print('1', curTranslationAIndex, numInter, translation)
    
#     # for p in scannerB:
#     #     setattr(p, attr, getattr(p, attr) * -1)
#     for p in scannerB:
#         p.x *= -1
    
#     curTranslationAIndex = -12
#     numInter = 0
#     while numInter < 12 and curTranslationAIndex < 11:
#         curTranslationAIndex += 1
#         translation = A[curTranslationAIndex] - B[11]
#         newScannerB = map(lambda p: p.translate(attr, translation), scannerB)
#         newB = sorted([getattr(p, attr) for p in newScannerB])
#         numInter = len(set(newB).intersection(A))
#         if numInter >= 12:
#             print('-1', curTranslationAIndex, numInter, translation)
    



def compareScannersOnX(scannerA, scannerB):
    # assume A to left of B
    xsA = sorted([p.x for p in scannerA])
    xsB = sorted([p.x for p in scannerB])

    curTranslationAIndex = -12
    numInter = 0
    while numInter < 12 and curTranslationAIndex < 11:
        curTranslationAIndex += 1
        translation = xsA[curTranslationAIndex] - xsB[11]
        newScannerB = map(lambda p: p.translateX(translation), scannerB)
        xsNewB = sorted([p.x for p in newScannerB])
        numInter = len(set(xsNewB).intersection(xsA))
        if numInter >= 12:
            print('1', curTranslationAIndex, numInter, translation)
    
    for p in scannerB:
        p.x *= -1
    
    xsA = sorted([p.x for p in scannerA])
    xsB = sorted([p.x for p in scannerB])

    curTranslationAIndex = -12

    numInter = 0
    while numInter < 12 and curTranslationAIndex < 11:
        curTranslationAIndex += 1
        translation = xsA[curTranslationAIndex] - xsB[11]
        newScannerB = map(lambda p: p.translateX(translation), scannerB)
        xsNewB = sorted([p.x for p in newScannerB])
        numInter = len(set(xsNewB).intersection(xsA))
        if numInter >= 12:
            print('-1', curTranslationAIndex, numInter, translation)

def compareScannersOnY(scannerA, scannerB, swap):
    # assume A to left of B
    ysA = sorted([p.y for p in scannerA])
    ysB = sorted([p.y for p in scannerB])

    curTranslationAIndex = -12
    numInter = 0
    while numInter < 12 and curTranslationAIndex < 11:
        curTranslationAIndex += 1
        translation = ysA[curTranslationAIndex] - ysB[11]
        newScannerB = map(lambda p: p.translateY(translation), scannerB)
        ysNewB = sorted([p.y for p in newScannerB])
        numInter = len(set(ysNewB).intersection(ysA))
        # print(translation)
        if numInter >= 12:
            print('1', curTranslationAIndex, numInter, translation)
            return translation * (-1 if swap else 1)
    
    for p in scannerB:
        p.y *= -1
    
    # ysA = sorted([p.y for p in scannerA])
    ysA = sorted([p.y for p in scannerA])
    ysB = sorted([p.y for p in scannerB])

    curTranslationAIndex = -12

    numInter = 0
    while numInter < 12 and curTranslationAIndex < 11:
        curTranslationAIndex += 1
        translation = ysA[curTranslationAIndex] - ysB[11]
        newScannerB = map(lambda p: p.translateY(translation), scannerB)
        ysNewB = sorted([p.y for p in newScannerB])
        numInter = len(set(ysNewB).intersection(ysA))
        # print(translation)
        if numInter >= 12:
            print('-1', curTranslationAIndex, numInter, translation)
            return translation * (1 if swap else -1)

    print(swap)            
    if not swap:
        compareScannersOnY(scannerB, scannerA, True)

        



f = open('testinput.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))

scanners = []
scannerNum = -1
for line in lines:
    if line.startswith('--- scanner'):
        scannerNum += 1
        scanners.append([])
    elif line != ' ' and line != '':
        xyz = line.split(',')
        l = Point(xyz[0], xyz[1], xyz[2])
        scanners[scannerNum].append(l)

for i in range(1, len(scanners)):
    print(compareScannersOnY(scanners[0], scanners[i], False))
# print(compareScannersOnX(scanners[0], scanners[2]))