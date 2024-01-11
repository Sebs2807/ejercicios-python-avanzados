class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None] * 0 for i in range(0)]

    def contenido_en(self, lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        self.vertices.append(v)
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas + 1) for i in range(columnas + 1)]
        for i in range(filas):
            for j in range(columnas):
                matriz_aux[i][j] = self.matriz[i][j]
        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, dirigida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        valor = 1
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor
        if not dirigida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

    def imprimir_matriz(self, m, booleano):
        cadena = "\n"

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " + ("........." * len(m))

        for i in range(len(m)):
            cadena += "\n" + str(self.vertices[i]) + " |"
            for j in range(len(m)):
                if booleano:
                    valor = m[i][j]
                    cadena += "\t" + (str(valor) if valor is not None else "0")
                else:
                    cadena += "\t" + ("0" if m[i][j] is None else "1")
        cadena += "\n"
        print(cadena)


    def imprimir_lista(self, lista_adyacencia):
        print("\n")
        for vertice, adyacentes in lista_adyacencia.items():
            adyacentes_str = ", ".join([f"{v}" for v in adyacentes])
            print(f"{vertice}: {adyacentes_str}")


    def matriz_a_lista_adyacencia(self):
        lista_adyacencia = {}
        for i in range(len(self.vertices)):
            lista_adyacencia[self.vertices[i]] = []
            for j in range(len(self.vertices)):
                if self.matriz[i][j] is not None:
                    lista_adyacencia[self.vertices[i]].append(self.vertices[j])
        return lista_adyacencia

    #Busqueda en matriz
    def busqueda_por_profundidad_matriz(self, inicio):
        if not(self.esta_en_vertices(inicio)):
            return None
        recorrido = []
        pila = [inicio]
        visitados = set()
        
        while pila:
            vertice_actual = pila.pop()

            if vertice_actual not in visitados:
                recorrido.append(vertice_actual)
                visitados.add(vertice_actual)

                for i in range(len(self.vertices)):
                    if self.matriz[self.vertices.index(vertice_actual)][i] is not None:
                        vertice_vecino = self.vertices[i]
                        if vertice_vecino not in visitados:
                            pila.append(vertice_vecino)

        return recorrido
    #Busqueda en lista
    def busqueda_por_profundidad_lista(self, inicio, visitados=None, recorrido=None):
        if visitados is None:
            visitados = set()
        if recorrido is None:
            recorrido = []

        visitados.add(inicio)
        recorrido.append(inicio)

        grafo = self.matriz_a_lista_adyacencia()
        for vecino in grafo.get(inicio, []):
            if vecino not in visitados:
                self.busqueda_por_profundidad_lista(vecino, visitados, recorrido)

        return recorrido

if __name__ == "__main__":
    g = Grafo()

    g.agregar_vertices("A")
    g.agregar_vertices("B")
    g.agregar_vertices("C")
    g.agregar_vertices("D")
    g.agregar_vertices("E")
    g.agregar_vertices("F")

    # # No dirigido.
    # g.agregar_arista("A", "B", False)
    # g.agregar_arista("B", "D", False)
    # g.agregar_arista("B", "C", False)
    # g.agregar_arista("C", "E", False)
    # g.agregar_arista("D", "E", False)
    # g.agregar_arista("D", "F", False)
    # g.agregar_arista("E", "F", False)

    # Dirigido.
    g.agregar_arista("A", "B", True)
    g.agregar_arista("B", "D", True)
    g.agregar_arista("B", "C", True)
    g.agregar_arista("C", "E", True)
    g.agregar_arista("D", "E", True)
    g.agregar_arista("D", "F", True)
    g.agregar_arista("E", "F", True)

    print("------------------------------------Matriz de Adyacencia:------------------------------------")
    g.imprimir_matriz(g.matriz, True)
    
    lista_adyacencia = g.matriz_a_lista_adyacencia()
    print("------------------------------------Lista de Adyacencia:------------------------------------")
    g.imprimir_lista(lista_adyacencia)

    inicio = "A"
    recorrido_dfs_matriz = g.busqueda_por_profundidad_matriz(inicio)
    recorrido_dfs_lista = g.busqueda_por_profundidad_lista(inicio)

    print("\nRecorrido DFS desde el vértice por matriz desde", inicio, ":")
    print(" -> ".join(recorrido_dfs_matriz))

    print("\nRecorrido DFS desde el vértice por lista desde", inicio, ":")
    print(" -> ".join(recorrido_dfs_lista))




    
    
