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
        print(xs, ys, zs)
    
    # def __sub__(self, other):
    #     # don't overlap in all 3 coords
    #     if self.x.start > other.x.end:
    #         return self
    #     elif self.x.end < other.x.start:
    #         return self
    #     elif self.y.start > other.y.end:
    #         return self
    #     elif self.y.end < other.y.start:
    #         return self
    #     elif self.z.start > other.z.end:
    #         return self
    #     elif self.z.end < other.z.start:
    #         return self
    #     # contained within other
    #     # x ([
    #     elif self.x.start >= other.x.start:
    #         # x ([])
    #         if self.x.end <= other.x.end:
    #             # x entirely within
    #             # x ([
    #             if self.y.start >= other.y.start:
    #                 # y ([])
    #                 if self.y.end <= other.y.end:
    #                     # y entirely within
    #                     # z ([
    #                     if self.z.start >= other.z.start:
    #                         # z ([])
    #                         if self.z.end <= other.z.end:
    #                             # z entirely within
    #                             return []
    #                         # z ([)]
    #                         else:
    #                             # extends in z dimension
    #                             return [Cube(deepcopy(self.x), deepcopy(self.y), (self.z - other.z)[0])]
    #                     # z [(
    #                     else:
    #                         # z [(])
    #                         if self.z.end <= other.z.end:
    #                             return [Cube(deepcopy(self.x), deepcopy(self.y), (self.z - other.z)[0])]
    #         # x )]
    #         else:
    #             return 

f = open('testinput.txt')
lines = f.readlines()
instrs = list(map(lambda x: x.strip('\n').split(' ') , lines))
instrs = list(map(lambda instr: list(map(lambda x:x.split(','), instr)), instrs))
instrs = [[*instr[0],  list(map(lambda x: x.split('=')[1].split('..'), instr[1]))] for instr in instrs]
instrs = [[instr[0], list(map(lambda x: list(map(int, x)), instr[1]))] for instr in instrs]
instrs = [[instr[0],  list(map(lambda xy: Interval(xy[0], xy[1]), instr[1]))]for instr in instrs]
instrs = [[instr[0],  Cube(instr[1][0], instr[1][1], instr[1][2])]for instr in instrs]
print(instrs)

cs = Cube(Interval(0,5),Interval(0,5),Interval(0,5)) - Cube(Interval(0,5), Interval(0,5), Interval(0,6))