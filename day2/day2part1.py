import functools

f = open('input.txt')
lines = map(lambda x: x.strip('\n'), f.readlines())
tuplelines = map(lambda x: x.split(' '), lines)
# print(tuplelines)
tuplelines = map(lambda xy: [xy[0], int(xy[1])], tuplelines)

horizontal = functools.reduce(lambda x, y: x+y[1] if y[0] == 'forward' else x, tuplelines, 0)
depth = functools.reduce(lambda x, y: x+y[1] if y[0] == 'down' else x-y[1] if y[0] == 'up' else x, tuplelines, 0)
print(horizontal * depth)