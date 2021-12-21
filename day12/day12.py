import copy

def getAdjacencyList(edges):
    adjList = dict()
    for edge in edges:
        if edge[0] not in adjList:
            adjList[edge[0]] = []
        adjList[edge[0]].append(edge[1])
    for edge in edges:
        if edge[1] not in adjList:
            adjList[edge[1]] = []
        adjList[edge[1]].append(edge[0])
    return adjList

def isBigCave(node):
    return node.isupper()

def isLeaf(node, adjList):
    return not node in adjList

def explore(node, adjList, stack):
    global hasDouble
    thisHasDouble = False
    if node == 'end':
        print(stack)
        paths.append(copy.deepcopy(stack))
        return stack[:len(stack)-1] 

    # if node in visited:
    #     return stack[:len(stack)-1] 
    if node in stack and not isBigCave(node):
        if hasDouble or node=='start':
            return stack 
        else:
            thisHasDouble = True
            hasDouble = True

    print('entering %s' % node)
    stack.append(node)
    print(stack)

    print('neighbours %s' % adjList[node])
    for child in adjList[node]:
        explore(child, adjList, copy.deepcopy(stack))

    visited.append(node)
    if thisHasDouble:
        hasDouble = False
    print('returning from %s' % node)
    return stack[:len(stack)-1] 

paths = []
visited = []
hasDouble = False

f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: ''.join(x),list(map(lambda x: list(x.strip('\n')), lines))))
edges = list(map(lambda x: x.split('-'), lines))

# print(edges)
print(getAdjacencyList(edges))
# print(isBigCave(getAdjacencyList(edges)['start'][1]))

explore('start', getAdjacencyList(edges), list())
for path in paths:
    print(path)
print(len(paths))