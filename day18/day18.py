import json
import math

class Node:
    def __init__(self, l, r, d, parent):
        if type(l) == list:
            self.l = Node(l[0], l[1], d+1, self)
        elif type(l) == Node:
            l.increaseDepth()
            self.l = l
        else:
            self.l = int(l)

        if type(r) == list:
            self.r = Node(r[0], r[1], d+1, self)
        elif type(r) == Node:
            r.increaseDepth()
            self.r = r
        else:
            self.r = int(r)
        self.d = d
        self.parent = parent
    
    def __repr__(self):
        return f"{self.d} :\n {self.d * '  '} {self.l} \n {self.d * '  '} {self.r}"
    
    def __str__(self):
        return f"[{self.l},{self.r}]"

    def increaseDepth(self):
        self.d += 1
        if type(self.l) == Node:
            self.l.increaseDepth()
        if type(self.r) == Node:
            self.r.increaseDepth()

    def split(self):
        if (type(self.l) == int) and (self.l >= 10):
            self.splitL()
            return True
        if (type(self.l) == Node):
            hasSplit = self.l.split()
            if hasSplit:
                return True
        if (type(self.r) == int) and (self.r >= 10):
            self.splitR()
            return True
        if (type(self.r) == Node):
            hasSplit = self.r.split()
            if hasSplit:
                return True
        return False
    
    def splitL(self):
        self.l = Node(math.floor(self.l/2), math.ceil(self.l/2), self.d+1, self)

    def splitR(self):
        self.r = Node(math.floor(self.r/2), math.ceil(self.r/2), self.d+1, self)
    
    def setPredecessor(self, i):
        # print('setting pred')
        if self.d==0:
            return
        if (self.parent.l != None) & (self.parent.l != self):
            if type(self.parent.l) == int:
                self.parent.l += i
                return
            cur = self.parent.l
            while type(cur.r) != int:
                cur = cur.r
            cur.r += i
        else:
            self.parent.setPredecessor(i)

    def setSuccessor(self, i):
        # print('setting succ')
        if self.d==0:
            return
        if (self.parent.r != None) & (self.parent.r != self):
            if type(self.parent.r) == int:
                self.parent.r += i
                return
            cur = self.parent.r
            while type(cur.l) != int:
                cur = cur.l
            cur.l += i
        else:
            self.parent.setSuccessor(i)

    def explode(self):
        if type(self.l) == Node:
            self.l = self.l.explode()
        if type(self.r) == Node:
            self.r = self.r.explode()
        if type(self.l) == int and (type(self.r) == int) and (self.d > 3):
            self.setPredecessor(self.l)
            self.setSuccessor(self.r)
            return 0
        return self

    def magnitude(self):
        l = 0
        r = 0
        if type(self.l) == int:
            l = 3 * self.l
        else:
            l = 3*self.l.magnitude()
        if type(self.r) == int:
            r = 2 * self.r
        else:
            r = 2 * self.r.magnitude()
        return l+r


def reduceSnailfish(num):
    print('\nreducing:\t', num)
    num.explode()
    print('after explode:\t', num)
    while num.split():
        print('after split:\t', num)
        num.explode()
        print('after explode:\t', num)

def parseSnailfishNum(snailfishNum):
    return Node(snailfishNum[0], snailfishNum[1], 0, None)

def add(num1, num2):
    n = Node(num1, num2, 0, None)
    num1.parent = n
    num2.parent = n
    return n

def split(num):
    return [math.floor(num/2), math.ceil(num/2)]

def sumList(l):
    s = parseSnailfishNum(l[0])
    for i in range(1,len(l)):
        t = parseSnailfishNum(l[i])
        s = add(s, t)
        reduceSnailfish(s)
    return s


f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: json.loads(x), lines))

# s = parseSnailfishNum([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])

# l = [[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]], [7,[5,[[3,8],[1,4]]]]]
l = lines

s =sumList(l)
print('\nfinal:\t\t', s)
print(s.magnitude())

bestIndex = [0,0]
bestScore = 0
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        suml = [l[i], l[j]]
        s = sumList(suml)
        if s.magnitude() > bestScore:
            bestScore = s.magnitude()
            bestIndex = [i,j]

        suml = [l[j], l[i]]
        s = sumList(suml)
        if s.magnitude() > bestScore:
            bestScore = s.magnitude()
            bestIndex = [j,i]


print(bestScore)