import functools

def isBiggerThanLast(x, y):
    return y > x


with open('input.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip('\n'), lines))
    lines = list(map(lambda x: int(x), lines))
    zipLines = list(zip(lines, lines[1:]))
    biggerList = list(map(lambda xy: isBiggerThanLast(xy[0],xy[1]), zipLines))
    print(len(list(filter(lambda x: x== True, biggerList))))