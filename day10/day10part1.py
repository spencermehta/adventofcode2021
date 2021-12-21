def consumeToken(s):
    print(s)
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
    print('consuming star')
    s = consumeToken(s[1:])
    if len(s) == 0:
        return 'incomplete'
    while s[0] in '[<{(':
        s = consumeToken(s)
    if s[0] == 'c':
        print('back up to star')
        return s[1:]
    elif s[0] in ']>})':
        return 'error %s expecting )' % s[0]
    else: 
        return s

def consumeParentheses(s):
    print('consuming parenthesis')
    s = consumeToken(s[1:])
    if len(s) == 0:
        return 'incomplete'
    while s[0] in '[<{(':
        s = consumeToken(s)
    if s[0] == ')':
        print('back up to parenthesis')
        return s[1:]
    elif s[0] in ']>}':
        return 'error %s expecting )' % s[0]
    else: 
        return s

def consumeSquareBrackets(s):
    print('consuming square bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        return 'incomplete'
    while s[0] in '[<{(':
        s = consumeToken(s)
    if s[0] == ']':
        print('back up to square bracket')
        return s[1:]
    elif s[0] in ')>}':
        return 'error %s expecting ]' % s[0]
    else: 
        return s

def consumeCurlyBrackets(s):
    print('consuming curly bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        return 'incomplete'
    while s[0] in '[<{(':
        s = consumeToken(s)
    if s[0] == '}':
        print('back up to curly bracket')
        return s[1:]
    elif s[0] in ')]>':
        return 'error %s expecting }' % s[0]
    else: 
        return s

def consumeTriangle(s):
    print('consuming triangle bracket')
    s = consumeToken(s[1:])
    if len(s) == 0:
        return 'incomplete'
    while s[0] in '[<{(':
        s = consumeToken(s)
    if s[0] == '>':
        print('back up to triangle bracket')
        return s[1:]
    elif s[0] in ')]}':
        return 'error %s expecting >' % s[0]
    else: 
        return s


f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
# print(lines)

# print(consumeToken('<{([([[(<>()){}]>(<<{{'))
# print(consumeToken('o{([(<{}[<>[]}>{[]{[(<()>c'))

errors = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}
for line in lines:
    line = consumeToken("o%sc" % line)
    print(line)
    if (line[0:5] == 'error'):
        errors[line[6]] +=1
    print('\n\n')

print(errors)

print(errors[')'] * 3 + errors[']'] * 57 + errors['}'] * 1197 + errors['>'] * 25137)
    