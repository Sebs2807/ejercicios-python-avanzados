def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = [[] for i in range(n + 1)]
    for x,y in cities:
        graph[x].append(y)
        graph[y].append(x)
    costo = 0
    visitados = [False] * (n + 1)
    
    def dfs(u,graph,visitados):
        visitados[u] = True
        ciudades = 1
        for v in graph[u]:
            if visitados[v] == False:
                ciudades += dfs(v,graph,visitados)
        return ciudades
    for v in range(1,n+1):
        if visitados[v] == False:
            ciudades = dfs(v,graph,visitados)
            costo1 = (ciudades - 1)* c_road + c_lib
            costo2 = (ciudades) * c_lib  
            costo += min(costo1,costo2)
    return costo
def main():
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')
