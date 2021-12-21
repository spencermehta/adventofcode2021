import functools

class Lanternfish:
    def __init__(self, daysLeft = 8, isNew = True):
        self.timer = daysLeft
        self.new = isNew
    
    def __str__(self):
        return "Lanterfish (%s, %s)" % (self.timer, self.new)

    def __repr__(self):
        return "Lanterfish (%s, %s)" % (self.timer, self.new)
    
    def passDay(self):
        if self.timer > 0:
            self.timer -= 1
            return [self]
        elif self.timer == 0:
            self.timer = 6
            lf = Lanternfish()
            return [self, lf]

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
initial = [int(num) for num in lines[0].split(',')]
lanternFish = list(map(lambda x: Lanternfish(x, False), initial))

for day in range(1,81):
    lanternFish = functools.reduce(lambda x, y: [*x, *(y.passDay())], lanternFish, [])
    print("%s: %s" % (day, len(lanternFish)))