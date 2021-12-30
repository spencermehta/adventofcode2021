f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
target = lines[0].replace(' ', '')
target = target.split(':')[1].split(',')
target = [t.split('=')[1] for t in target]
target = [list(map(int, t.split('..'))) for t in target]
print(target)

x_range = [1, target[0][1]]
y_range = [target[1][0],abs(target[1][0])]
print(x_range, y_range)

total = 0
for xstart in range(x_range[0], x_range[1] + 1):
    for ystart in range(y_range[0], y_range[1] + 1):
        x = y = 0
        vx, vy = xstart, ystart

        while x <= target[0][1] and y >= target[1][0]:
            if x >= target[0][0] and y <= target[1][1]:
                total += 1
                break

            x, y = (x + vx, y + vy)
            vy -= 1

            if vx > 0:
                vx -= 1

print(total)
