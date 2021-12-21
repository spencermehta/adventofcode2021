def cost(x, target):
    diff = abs(x-target)
    diffRange = list(range(0, diff +1))
    return sum(diffRange)

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
horizontals = [int(num) for num in lines[0].split(',')]
print(len(horizontals))

costs = ['' for i in range(0,max(horizontals))]
for i in range(0, max(horizontals)):
    costs[i] = sum(list(map(lambda x: cost(x, i), horizontals)))

print(len(costs))
# print(costs)
# print(costs.index(min(costs)), min(costs))