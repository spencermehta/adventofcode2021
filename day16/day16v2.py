import math
import numpy as np

class Packet:
    def __init__(self, v, t):
        self.v = v
        self.t = t

class Literal(Packet):
    def __init__(self, v, t, val):
        self.val = val
        super().__init__(v, t)

    def version(self):
        return self.v
    
    def getVal(self):
        return binToDec(self.val)
    
    def length(self):
        return (math.floor(len(self.val) / 4) * 5) + 6

    def __repr__(self):
        return f"Lit [{self.v}, {self.t}] {self.length()} ({self.val}/{self.getVal()})"

class Operator(Packet):
    def __init__(self, v, t, ltid, children):
        self.ltid = ltid
        self.children = children
        super().__init__(v, t)
    
    def getVal(self):
        print(self.t)
        if self.t == 0:
            return sum(map(lambda x: x.getVal(), self.children))
        elif self.t == 1:
            return multiplyList(map(lambda x: x.getVal(), self.children))
        elif self.t == 2:
            return min(map(lambda x: x.getVal(), self.children))
        elif self.t == 3:
            return max(map(lambda x: x.getVal(), self.children))
        elif self.t == 5:
            return 1 if self.children[0].getVal() > self.children[1].getVal() else 0
        elif self.t == 6:
            return 1 if self.children[0].getVal() < self.children[1].getVal() else 0
        elif self.t == 7:
            return 1 if self.children[0].getVal() == self.children[1].getVal() else 0

    def version(self):
        return self.v + sum(map(lambda x: x.version(), self.children))
    
    def length(self):
        if self.ltid == '0':
            return sum(map(lambda x: x.length(), self.children)) + 7 + 15
        else:
            return sum(map(lambda x: x.length(), self.children)) + 7 + 11
    
    def __repr__(self):
        return f"Op [{self.v}, {self.t}, {self.ltid}] {self.length()} ({self.children})"

def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result

def hexToBin(hexa):
    h_size = len(hexa) * 4
    return  ( bin(int(hexa, 16))[2:] ).zfill(h_size)

def binToDec(bin):
    scale = 2
    return int(bin, scale)

def parseLiteral(v, t, litstr):
    # print('parsing literal', v, t)
    binstr = ''
    i = 0
    while True:
        continueBit = litstr[i]
        fragment = litstr[i+1:i+5]
        binstr += fragment
        if continueBit == '0':
            break
        else:
            i += 5
    lit = Literal(v, t, binstr)
    # print('parsed literal', lit)
    return lit

def parseOperator(v, t, opstr):
    ltid = opstr[0]
    # print('parsing operator', v, t, ltid)
    if ltid == '0':
        children = []
        length = binToDec(opstr[1:16])
        # print('l', length)
        childstr = opstr[16:]
        i = 0
        while i < length:
            child = parsePacket(childstr[i:])
            i += child.length()
            children.append(child)
        op = Operator(v, t, ltid, children)
        # print('parsed operator', op, op.length())
        return op
    else:
        children = []
        num = binToDec(opstr[1:12])
        # print('n', num)
        childstr = opstr[12:]
        i = 0
        while len(children) < num:
            # print('i', i)
            # print(childstr[i:])
            child = parsePacket(childstr[i:])
            i += child.length()
            children.append(child)
        op = Operator(v, t, ltid, children)
        # print('parsed operator', op, op.length())
        return op

def parsePacket(binstr):
    v = binToDec(binstr[:3])
    t = binToDec(binstr[3:6])

    if (t == 4):
        return parseLiteral(v, t, binstr[6:])
    else:
        return parseOperator(v, t, binstr[6:])

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
hexa = lines[0]
print(hexToBin(hexa))
p =parsePacket(hexToBin(hexa))
print('\n\n')
print(p)
print(p.version())
print(p.getVal())