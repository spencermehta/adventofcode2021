from dataclasses import dataclass

@dataclass
class Instr:
    op: str
    a: str
    b: str = None

def get_val(x: str):
    if x.strip('-').isnumeric():
        return int(x)
    elif x in registers.keys():
        return registers[x]
    else:
        print('error')

def parse_instr(instr: 'Instr'):
    if instr.op == 'inp':
        global inputs
        registers[instr.a] = inputs[0]
        inputs = inputs[1:]
    elif instr.op == 'add':
        registers[instr.a] = get_val(instr.a) + get_val(instr.b)
    elif instr.op == 'mul':
        registers[instr.a] = get_val(instr.a) * get_val(instr.b)
    elif instr.op == 'div':
        # so ugly lol
        registers[instr.a] = get_val(instr.a) // get_val(instr.b) if get_val(instr.a) > 0 else - (abs(get_val(instr.a)) // get_val(instr.b))
    elif instr.op == 'mod':
        registers[instr.a] = get_val(instr.a) % get_val(instr.b)
    elif instr.op == 'eql':
        registers[instr.a] = 1 if get_val(instr.a) == get_val(instr.b) else 0

def parse_input(inp: int): 
    registers = {key: 0 for key in ['w','x','y','z']}
    global inputs
    inputs = [int(c) for c in str(inp)]
    for instr in instrs:
        parse_instr(instr)
    return registers

f = open('input.txt')
lines = f.readlines()
instrs = list(map(lambda x: x.strip('\n').split(' ') , lines))
instrs = [Instr(*x) for x in instrs]

# globals
registers = {key: 0 for key in ['w','x','y','z']}
inputs = []

for inp in range(99999999999999, 11111111111111, -1):
    print(inp)
    if '0' not in str(inp):
        res = parse_input(inp)
        if registers['z'] == 0:
            print(inp)
            break