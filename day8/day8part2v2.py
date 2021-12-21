f = open('input.txt')
lines = f.readlines()
lines = list(map(lambda x: x.strip('\n'), lines))
lines = list(map(lambda x: x.split("|"), lines))
lines = list(map(lambda xs: [xs[0].split(), xs[1].split()], lines))

visited = set()

encoding = [['a','b','c','d','e','f','g'] for i in range(0,7)]

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, encoding, 0)