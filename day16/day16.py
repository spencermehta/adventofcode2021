import math

class Packet:
    def __init__(self, version, typeId):
        self.version = version
        self.typeId = typeId
        self.children = []
    
    def __repr__(self):
        return "Packet v%s t%s (%s)" % (self.version, self.typeId, self.children)

class Literal(Packet):
    def __init__(self, version, typeId, literal, literalBin):
        self.literal = literal
        self.literalBin = literalBin
        super().__init__(version, typeId)

    def length(self):
        return 6+ math.floor(len(self.literalBin)/4) * 5
    
    def isTrailing(self):
        return False

    def __repr__(self):
        return "Literal v%s t%s (%s/%s)" % (self.version, self.typeId, self.literal, self.literalBin)

class Operator(Packet):
    def __init__(self, version, typeId, lengthTypeId, subPacketlength, numSubpackets):
        self.lengthTypeId = lengthTypeId
        self.subPacketLength = subPacketlength
        self.numSubpackets = numSubpackets
        self.children = []
        super().__init__(version, typeId)
    
    def length(self):
        return 7 + (15 if self.lengthTypeId == 0 else 11) + sum(list(map(lambda x: x.length(), self.children)))

    def isTrailing(self):
        return False
    
    def __repr__(self):
        if self.lengthTypeId == '0':
            return "Operator v%s t%s lt%s ls%s (%s)" % (self.version, self.typeId, self.lengthTypeId, self.subPacketLength, self.children)
        return "Operator v%s t%s lt%s ns%s (%s)" % (self.version, self.typeId, self.lengthTypeId, self.numSubpackets, self.children)

def parseLiteral(version, typeId, literal):
    print('parsing literal')
    i=0
    value = ''
    while True:
        fragment = literal[i+1:i+5]
        value += fragment
        # print('lit i', i, literal[i:i+5])
        if literal[i] == '0':
            break
        i+=5
    print('v', value)
    return Literal(version, typeId, binToDec(value), value)

def parsePacketListLength(subpackets, subpacketLength):
    print('parsing packetlistlength')
    i=0
    packs = []
    while i < subpacketLength:
        p = parsePacket(subpackets[i:])
        packs.append(p)
        i += p.length()
    print('parsed packetlistlength')
    return packs

def parsePacketListNum(subpackets, numSubpackets):
    print('parsing packetlistnum')
    packs = []
    i=0
    j=0
    while j < numSubpackets:
        print(j, numSubpackets)
        p = parsePacket(subpackets[i:])
        packs.append(p)
        i += p.length()
        j+=1
    print('parsed packetlistnum')
    return packs

def parseOperator(version, typeId, operator):
    print('parsing operator')
    lengthTypeId = operator[0]
    subpacketLength = None
    numSubpackets = None
    if lengthTypeId == '0':
        subpacketLength = binToDec(operator[1:16])
        op = Operator(version, typeId, lengthTypeId, subpacketLength, None)
        subpackets = operator[16:]
        op.children = parsePacketListLength(subpackets, subpacketLength)
    elif lengthTypeId == '1':
        numSubpackets = binToDec(operator[1:12])
        op = Operator(version, typeId, lengthTypeId, None, numSubpackets)
        subpackets = operator[12:]
        op.children = parsePacketListNum(subpackets, numSubpackets)
    else:
        raise Exception('invalid lenghTypeId')

    return op


def parsePacket(packet):
    version = binToDec(packet[:3])
    typeId = binToDec(packet[3:6])

    if typeId == 4:
        literal = parseLiteral(version, typeId, packet[6:])
        print('parsed lit packet')
        return literal
    else:
        op = parseOperator(version, typeId, packet[6:])
        print('parsed opp packet')
        return op

    # return myPacket

def binToDec(bin):
    scale = 2
    return int(bin, scale)

def hexToBin(hexa):
    # scale = 16
    # num_of_bits = 8
    # return bin(int(hexa, scale))[2:].zfill(num_of_bits)
    h_size = len(hexa) * 4
    return  ( bin(int(hexa, 16))[2:] ).zfill(h_size)



f = open('testinput.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
hexa = lines[0]

# print(hexToBin(hexa))
print(parsePacket(hexToBin(hexa)))