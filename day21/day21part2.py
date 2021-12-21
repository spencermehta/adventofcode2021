import copy

def move(p, r):
    return ((p-1 + r) % 10)+1

def roll(spaces, scores, player, arr):
    if len(arr) == 3:
        play(copy.deepcopy(spaces), copy.deepcopy(scores), player, sum(arr))
        return
    roll(copy.deepcopy(spaces), copy.deepcopy(scores), player, [*arr, 1])
    roll(copy.deepcopy(spaces), copy.deepcopy(scores), player, [*arr, 2])
    roll(copy.deepcopy(spaces), copy.deepcopy(scores), player, [*arr, 3])

def play(spaces, scores, player, r):
    m = move(spaces[player], r)

    spaces[player] = m
    scores[player] += m
    if scores[player] >= 21:
        wins[player] += 1
        # print(f"player {player} wins")
        return player
    
    nextPlayer = 0 if player == 1 else 1

    roll(copy.deepcopy(spaces), copy.deepcopy(scores), nextPlayer, [])



f = open('testinput.txt')
lines = f.readlines()
spaces = list(map(lambda x: int(x.strip('\n').split()[-1]) , lines))

scores = [0,0]
wins = [0,0]

i = 1
rolls = 0

roll(copy.deepcopy(spaces), copy.deepcopy(scores), 0, [])

print(wins)