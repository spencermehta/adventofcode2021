import functools

def passDay(lf): 
    zeros = lf.count(0)
    newLf = list(map(lambda x: x-1 if x > 0 else 6, lf))
    for zero in range(0, zeros):
        newLf.append(8)
    # newNewLf = [*newLf, *[8 for zero in range(0, zeros)]]
    return newLf

f = open('testinput.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lanternFish = [int(num) for num in lines[0].split(',')]

for day in range(1,257):
    lanternFish = passDay(lanternFish)
    print("%s: %s" % (day, len(lanternFish)))