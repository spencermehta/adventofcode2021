
def roll():
    global i, rolls
    j = i + (i+1) + (i+2)
    i += 3
    rolls += 3
    return j

def move(p):
    return ((p-1 + roll()) % 10)+1

f = open('input.txt')
lines = f.readlines()
spaces = list(map(lambda x: int(x.strip('\n').split()[-1]) , lines))

scores = [0,0]

i = 1
rolls = 0


while all([score < 1000 for score in scores]):
    for q in range(0, len(scores)):
        m = move(spaces[q])
        spaces[q] = m
        scores[q] += m
        if scores[q] >= 1000:
            break

print(scores, rolls)
print(min(scores) * rolls)