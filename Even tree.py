def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = [[] for i in range(t_nodes + 1)]
    for x,y in zip(t_from,t_to):
        graph[x].append(y)
        graph[y].append(x)
    count = [0] * (t_nodes + 1)

    def dfs(u,graph,count):
        count[u] = 1
        removed_edges = 0
        for v in graph[u]:
            if count[v] == 0:
                removed_edges += dfs(v,graph,count)
                count[u] += count[v]
                if count[v] % 2 == 0:
                    removed_edges += 1
        return removed_edges
    return dfs(1,graph,count)
def main():
    t_nodes, t_edges = map(int, input().rstrip().split())
    t_from = [0] * t_edges
    t_to = [0] * t_edges
    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())
    res = evenForest(t_nodes, t_edges, t_from, t_to)
    print(res)
main()