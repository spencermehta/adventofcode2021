import copy

def uniqueLetters(template, rules):
    map = set()
    for c in template:
        map.add(c)
    for rule in rules:
        for c in rule[0]:
            map.add(c)
        map.add(rule[1])
    return map

def getCombinations(letters):
    return [val1+val2 for val1 in letters for val2 in letters]

def readString(string, combs):
    for i in range(len(string)-1):
        a = string[i]
        b = string[i+1]
        ab = a + b
        combs[ab] += 1

def transferCombs(combs, defaultCombs):
    newCombs = copy.deepcopy(defaultCombs)
    for key in combs.keys():
        if key in rules.keys():
            n = combs[key]
            c = rules[key]
            newCombs[key[0] + c] += n
            newCombs[c + key[1]] += n
    return newCombs

def elementCount(e, combs):
    count = 0
    for key in combs.keys():
        if count == 0:
            if e == key[0]:
                n = combs[key]
                count += n
        if e == key[1]:
            n = combs[key]
            count += n
    return count

def mostCommonElement(combs, letters):
    return max(list(map(lambda x: elementCount(x, combs), letters)))

def leastCommonElement(combs, letters):
    return min(list(map(lambda x: elementCount(x, combs), letters)))


f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))

template = lines[0]
rules = lines[2:]
rules = [rule.split(' -> ') for rule in rules]
rules = dict(rules)
# print(rules)

# print(ruleMap)
# print(template)
# print(rules)

letters = uniqueLetters(template, rules)
combinations = getCombinations(letters)
combinationNumbers = [(c, 0) for c in combinations]
# print(combinationNumbers)

defaultCombs = dict(combinationNumbers)
combs = dict(combinationNumbers)
# print(combs)

readString(template, combs)
print(combs, '\n')

for i in range(0,40):
    combs = transferCombs(combs, defaultCombs)
    print(combs)

# print(elementCount('N', combs))
tot = sum(combs.values())
mc = mostCommonElement(combs, letters)
lc = leastCommonElement(combs, letters)
print(mc - lc)
