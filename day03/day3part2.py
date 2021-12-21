import functools
f = open('input.txt')
lines = map(lambda x: x.strip('\n'), f.readlines())
lines = map(lambda x: [char for char in x], lines)
pivotLines = [[row[i] for row in lines] for i in range(len(lines[0]))]

gammaModes =[max(x, key=x.count) for x in pivotLines]
epsilonModes =[min(x, key=x.count) for x in pivotLines]
# print(gammaModes, epsilonModes)

ogr1 = [row for row in lines if row[0] == gammaModes[0]]

ogr = lines
# print(len(ogr), len(gammaModes), len(epsilonModes))
for i in range(0,len(lines[0])):
    print(i)
    ogr = [row for row in ogr if row[i] == gammaModes[i]]
    # print(len(ogr))
    # print(len(ogr[0]))
    pivotOgr = [[row[i] for row in ogr] for i in range(len(ogr[0]))]
    gammaModes =[max(x, key=x.count) if x.count('1') != x.count('0') else '1' for x in pivotOgr]
    epsilonModes =[min(x, key=x.count) if x.count('1') != x.count('0') else '0' for x in pivotOgr]
    print(pivotOgr[9])
    print(gammaModes[9])
    print(max(pivotOgr[9], key=pivotOgr[9].count))
    print(min(pivotOgr[9], key=pivotOgr[9].count))
    print('\n')
    if len(ogr) == 1:
        break
    # print(pivotOgr[4], gammaModes[4], epsilonModes[4])
print(ogr)
[ogr] = ogr
ogrDec = int(functools.reduce(lambda x,y: x+y, ogr, ''), 2)
print('\n')


gammaModes =[max(x, key=x.count) for x in pivotLines]
epsilonModes =[min(x, key=x.count) for x in pivotLines]
csr = lines
# print(len(csr), len(gammaModes), len(epsilonModes))
for i in range(0,len(lines[0])):
    csr = [row for row in csr if row[i] == epsilonModes[i]]
    pivotCsr = [[row[i] for row in csr] for i in range(len(csr[0]))]
    gammaModes =[max(x, key=x.count) if x.count('1') != x.count('0') else '1' for x in pivotCsr]
    epsilonModes =[min(x, key=x.count) if x.count('1') != x.count('0') else '0' for x in pivotCsr]
    if len(csr) == 1:
        break
    # print(pivotCsr[i], gammaModes[i], epsilonModes[i])
print(csr)
[csr] = csr
csrDec = int(functools.reduce(lambda x,y: x+y, csr, ''), 2)

print(csrDec * ogrDec)