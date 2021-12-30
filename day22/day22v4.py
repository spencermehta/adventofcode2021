import math
from copy import deepcopy

class Interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self) -> str:
        return f"[{self.start}..{self.end}]"

    def length(self) -> int:
        return abs((self.end+1) - self.start)

    def __sub__(self, other):
        # ()[]
        if self.start > other.end:
            return self
        # []()
        elif other.start > self.end:
            return self
        # )]
        elif self.end > other.end:
            # [()]
            if self.start < other.start:
                return [Interval(self.start, other.start-1), Interval(other.end+1, self.end)]
            # ([)]
            else:
                return [Interval(other.end+1, self.end)]
        # ])
        else:
            # ([])
            if self.start >= other.start:
                return []
            # [(])
            else:
                return [Interval(self.start, other.start-1)]
            

class Cube():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self) -> str:
        return f"Cube ({self.x}, {self.y}, {self.z})"
    
    def area(self):
        return self.x.length() * self.y.length() * self.z.length()
    
    def __sub__(self, other):
        xs = self.x - other.x
        ys = self.y - other.y
        zs = self.z - other.z

        subCubes = []

        for x in xs:
            subCubes.append(Cube(x, self.y, self.z))


        #     for y in ys:
        #         subCubes.append(Cube(x, y, self.z))
        
        #     for z in zs:
        #         subCubes.append(Cube(x, self.y, z))
        
        # for y in ys:
        #     for z in zs:
        #         subCubes.append(Cube(self.x, y, z))

        # for y in ys:
        #     subCubes.append(Cube(self.x, y, self.z))

        # for z in zs:
        #     subCubes.append(Cube(self.x, self.y, z))
        
        return subCubes


f = open('testinput.txt')
lines = f.readlines()
instrs = list(map(lambda x: x.strip('\n').split(' ') , lines))
instrs = list(map(lambda instr: list(map(lambda x:x.split(','), instr)), instrs))
instrs = [[*instr[0],  list(map(lambda x: x.split('=')[1].split('..'), instr[1]))] for instr in instrs]
instrs = [[instr[0], list(map(lambda x: list(map(int, x)), instr[1]))] for instr in instrs]
instrs = [[instr[0],  list(map(lambda xy: Interval(xy[0], xy[1]), instr[1]))]for instr in instrs]
instrs = [[instr[0],  Cube(instr[1][0], instr[1][1], instr[1][2])]for instr in instrs]

cs = Cube(Interval(0,1),Interval(0,1),Interval(0,0)) - Cube(Interval(0,0), Interval(0,0), Interval(0,0))
nc = instrs[1][1] - instrs[0][1]

for c in cs:
    print(c)
    print(c.area())