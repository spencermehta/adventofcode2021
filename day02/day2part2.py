import functools
import numpy

f = open('input.txt')
lines = map(lambda x: x.strip('\n'), f.readlines())
tuplelines = map(lambda x: x.split(' '), lines)
# print(tuplelines)
tuplelines = map(lambda xy: [xy[0], int(xy[1])], tuplelines)

vals = [0,0,0]
def move(command, n):
    if command == "forward":
        vals[0] += n
        vals[1] += (vals[2] * n)
    if command == "down":
        vals[2] += n
    if command == "up":
        vals[2] -= n

map(lambda y: move(y[0], y[1]), tuplelines)
print(vals)
print(vals[0] * vals[1])