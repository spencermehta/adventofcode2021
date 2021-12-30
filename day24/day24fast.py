def solve(w,z):
    global inputs
    w = int(inputs[0])
    inputs = inputs[1:]
    z *= 26
    z += w+1
    return w,z

inputs = [int(c) for c in str('99999999999999')]

for inp in range(99999999999999, 11111111111111, -1):
    print(inp)
    inputs = [int(c) for c in str(inp)]
    w,z = 0,0
    for i in range(0,14):
        w,z = solve(w,z)
    if z == 0:
        print(inp, w,z)
        break