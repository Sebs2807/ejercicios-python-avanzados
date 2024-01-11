def journeyToMoon(n, astronaut):
    graph = [[] for i in range(n)]
    for x,y in astronaut:
        graph[x].append(y)
        graph[y].append(x)
    visitados = [False] * n
    parejas = n * (n - 1) // 2
    
    def dfs(u,graph,visitados):
        visitados[u] = True
        vertices = 1
        for v in graph[u]:
            if visitados[v] == False:
                vertices += dfs(v,graph,visitados)
        return vertices
    for v in range(n):
        if visitados[v] == False:
            personas = dfs(v,graph,visitados)
            parejas -= personas * (personas - 1) // 2        
    return parejas

def main():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    print(str(result) + '\n')