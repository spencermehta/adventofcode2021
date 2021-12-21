import copy
from collections import Counter

def move(p, r):
    return ((p-1 + r) % 10)+1

def roll():
    # return Counter([i+j+k for k in range(1,4) for j in range(1,4) for i in range(1,4)])
    rs = [i+j+k for k in range(1,4) for j in range(1,4) for i in range(1,4)]
    return set([(r, rs.count(r)) for r in rs])


def play(spaces, scores, player, r, instances):
    print(wins)
    m = move(spaces[player], r)
    
    spaces[player] = m
    scores[player] += m
    if scores[player] >= 21:
        wins[player] += instances
        # print(f"player {player} wins")
        return player
    
    nextPlayer = 0 if player == 1 else 1

    for (newR, newInstances) in roll():
        play(copy.deepcopy(spaces), copy.deepcopy(scores), nextPlayer, newR, instances*newInstances)



f = open('testinput.txt')
lines = f.readlines()
spaces = list(map(lambda x: int(x.strip('\n').split()[-1]) , lines))

scores = [0,0]
wins = [0,0]

i = 1
rolls = 0

# roll(copy.deepcopy(spaces), copy.deepcopy(scores), 0, [])

for (newR, newInstances) in roll():
    play(copy.deepcopy(spaces), copy.deepcopy(scores), 0, newR, 1*newInstances)

print(wins)
