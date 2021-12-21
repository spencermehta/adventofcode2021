import math
incomplete = ''

def consumeToken(s):
    print(s)
    if len(s) == 0:
        return ''
    if s[0] == '(':
        return consumeParentheses(s)
    elif s[0] == ')':
        return s
    elif s[0] == '[':
        return consumeSquareBrackets(s)
    elif s[0] == ']':
        return s
    elif s[0] == '[':
        return consumeSquareBrackets(s)
    elif s[0] == ']':
        return s
    elif s[0] == '{':
        return consumeCurlyBrackets(s)
    elif s[0] == '}':
        return s
    elif s[0] == '<':
        return consumeTriangle(s)
    elif s[0] == '>':
        return s
    elif s[0] == 'o':
        return consumeStar(s)
    elif s[0] == 'c':
        return s
    # else: 
    #     return s

def consumeStar(s):
    global incomplete
    print('consuming star')
    s = consumeToken(s[1:])
    if len(s) == 0:
        incomplete +='c'
        return ''
    while s[0] in '[<{(':
        s = consumeToken(s)
        if len(s) == 0:
            incomplete +='c'
            return ''
    if s[0] == 'c':
        print('back up to star')
        return s[1:]
    elif s[0] in ']>})':
        return 'error %s expecting c' % s[0]
    else: 
        return s

def consumeParentheses(s):
    global incomplete
    print('consuming parenthesis')
    s = consumeToken(s[1:])
    if len(s) == 0:
        print('incomplete')
        incomplete +=')'
        return ''
    while s[0] in '[<{(':
        s = consumeToken(s)
        if len(s) == 0:
            incomplete +=')'
            return ''
    if s[0] == ')':
        print('back up to parenthesis')
        return s[1:]
    elif s[0] in ']>}':
        return 'error %s expecting )' % s[0]
    else: 
        return s

def consumeSquareBrackets(s):
    global incomplete
    print('consuming square bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        incomplete += ']'
        return ''
    while s[0] in '[<{(':
        s = consumeToken(s)
        if len(s) == 0:
            incomplete += ']'
            return ''
    if s[0] == ']':
        print('back up to square bracket')
        return s[1:]
    elif s[0] in ')>}':
        return 'error %s expecting ]' % s[0]
    else: 
        return s

def consumeCurlyBrackets(s):
    global incomplete
    print('consuming curly bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        incomplete += '}'
        return ''
    while s[0] in '[<{(':
        s = consumeToken(s)
        if len(s) == 0:
            incomplete += '}'
            return ''
    if s[0] == '}':
        print('back up to curly bracket')
        return s[1:]
    elif s[0] in ')]>':
        return 'error %s expecting }' % s[0]
    else: 
        return s

def consumeTriangle(s):
    global incomplete
    print('consuming triangle bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        incomplete += '>'
        return ''
    while s[0] in '[<{(':
        s = consumeToken(s)
        if len(s) == 0:
            incomplete += '>'
            return ''
    if s[0] == '>':
        print('back up to triangle bracket')
        return s[1:]
    elif s[0] in ')]}':
        return 'error %s expecting >' % s[0]
    else: 
        return s

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def incompleteScore(incs):
    score = 0
    for char in incs:
        print(len(char))
        if char == 'c':
            return score
        score *= 5
        score += scores[char]
    return score

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
# print(lines)

# print(consumeToken('o[({(<(())[]>[[{[]{<()<>>'))
# print('incompletes', incomplete)
# print(consumeToken('o{([(<{}[<>[]}>{[]{[(<()>c'))


myScores = []
for line in lines:
    incomplete = ''
    line = consumeToken("o%s" % line)
    print(line)
    print('incompletes', incomplete)
    if (len(incomplete)> 0):
        print('inc')
        score = incompleteScore(incomplete)
        print(score)
        myScores.append(score)
    print('\n\n')

sortedScores = sorted(myScores)
print(sortedScores)
print(sortedScores[math.floor(len(sortedScores)/2)])

# print(errors)

# print(errors[')'] * 3 + errors[']'] * 57 + errors['}'] * 1197 + errors['>'] * 25137)
    