from collections import deque
def bfs(n,m,edges,s):
    graph = [[] for i in range(n + 1)]
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [False] * (n + 1)
    distances = [-1] * (n + 1)
    q = deque([(s,0)])
    distances[s] = 0
    visited[s] = True
    
    while q:
        u,w = q.popleft()
        for v in graph[u]:
            if visited[v] == False:
                distances[v] = w + 6
                visited[v] = True
                q.append(v,w + 6)
    distances.remove(0)
    return distances[1:]
def main():
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        print(' '.join(map(str, result)))
main()