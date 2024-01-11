def busqueda_por_profundidad_lista(inicio,grafo,visitados,recorrido):
    visitados.add(inicio)
    recorrido.append(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            busqueda_por_profundidad_lista(vecino,grafo,visitados,recorrido)

    return recorrido
def main():
    n = int(input())
    grafo = {i:[] for i in range(1,(2*n) + 1)}
    vertices = []
    for _ in range(n):
        vertices.append(list(map(int,input().rstrip().split())))
    for x,y in vertices:
        grafo[x].append(y)
        grafo[y].append(x)
    resultado = []
    for i in grafo.keys():
        total = len(busqueda_por_profundidad_lista(i,grafo,visitados=set(),recorrido=[]))
        if total != 1:
            resultado.append(total)
    print(min(resultado),max(resultado))
main()