peso_total=dict()

nodo_padre=dict()

diferencia_min=[float('inf')]

def dfs_iterative(G, s, weights):
    total = sum(weights)

    stack = [s]
    visited = set()

    while stack:
        vertice = stack[-1]
        if vertice in visited:
            peso_total[vertice]=weights[vertice-1]
            for c in G[vertice]:
                if nodo_padre.get(c,-1)==vertice:
                    peso_total[vertice]+=peso_total[c]
            diferencia_min[0]=min(
                diferencia_min[0],
                abs(total-2*peso_total[vertice])
            )
            stack.pop()
            continue
        visited.add(vertice)
        for vecino in G[vertice]:
            if vecino not in visited:
                nodo_padre[vecino]=vertice
                stack.append(vecino)
    
    return visited

def setGraph(cant_nodos, aristas):
    g=dict()

    for _t,_e in aristas:
        if _t not in g.keys():
            g[_t]=[_e]
        else:
            g[_t].append(_e)
        if _e not in g.keys():
            g[_e]=[_t]
        else:
            g[_e].append(_t)
    
    g.update({k:[] for k in range(1,cant_nodos+1) if k not in g.keys()})
    
    return g


def cutTheTree(nodes, aristas):
    G=setGraph(len(nodes),aristas)
    print(G)
    dfs_iterative(G,1,nodes)
    return diferencia_min[0]

if __name__ == '__main__':

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    aristas = []

    for _ in range(n - 1):
        aristas.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, aristas)

    print(str(result) + '\n')
