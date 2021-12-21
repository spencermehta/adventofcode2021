def progressDay(dayCounts):
    zeros = dayCounts[0]
    for i in range(1, 9):
        dayCounts[i-1] = dayCounts[i]
    dayCounts[8] = 0
    dayCounts[6] += zeros
    dayCounts[8] += zeros
    return dayCounts
    
f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lanternFish = [int(num) for num in lines[0].split(',')]

dayCounts = dict.fromkeys(range(0,9), 0)

for fish in lanternFish:
    dayCounts[fish] += 1

for day in range(1,257):
    dayCounts = progressDay(dayCounts)
    print("%s: %s" % (day, sum(dayCounts.values())))
