import functools
f = open('input.txt')
lines = map(lambda x: x.strip('\n'), f.readlines())
lines = map(lambda x: [char for char in x], lines)
pivotLines = [[row[i] for row in lines] for i in range(len(lines[0]))]
gamma = list(map(lambda x: max(x, key=x.count), pivotLines))
gammaBin = functools.reduce(lambda x,y: x+y, gamma, '')
gammaDec = int(gammaBin, 2)

epsilon = list(map(lambda x: min(x, key=x.count), pivotLines))
epsilonBin = functools.reduce(lambda x,y: x+y, epsilon, '')
epsilonDec = int(epsilonBin, 2)
print(gammaDec * epsilonDec) 