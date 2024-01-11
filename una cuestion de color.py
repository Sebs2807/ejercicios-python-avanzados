def verificador(grafo,colores,n,visitados):
    visitados.add(n)
    valor = True
    for vecino in grafo.get(n,[]):
        if colores[n] == colores[vecino]:
            valor = False
            return valor
        if vecino not in visitados:
            verificador(grafo,colores,n + 1,visitados)
    return valor
    
def coloreador(inicio,grafo,colores,visitados):
    visitados.add(inicio)
    for vecino in grafo.get(inicio,[]):
        if colores[inicio] == "AZUL":
            colores[vecino] = "ROJO"
        if colores[inicio] == "ROJO":
            colores[vecino] = "AZUL"
        if vecino not in visitados:
            coloreador(vecino,grafo,colores,visitados)
    return colores
        
def main():
    resultado = []
    while True:
        conexiones = []
        n = int(input())
        if n == 0:
            break
        grafo = {i:[] for i in range(n)}
        for _ in range(int(input())):
            conexiones.append(list(map(int,input().split())))
        for x,y in conexiones:
            grafo[x].append(y)
            grafo[y].append(x)
        colores = {}
        colores[0] = "AZUL"
        diccionario = coloreador(0,grafo,colores,visitados=set())
        resultado.append(verificador(grafo,diccionario,n = 0,visitados = set()))
    for i in resultado:
        if not i:
            print(f"NOT BICOLORABLE.")
        else:
            print("BICOLORABLE.")
main()