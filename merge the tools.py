class Conjunto_disyunto():
    def __init__(self):
        self.conjunto = []

    def crea_conjunto(self, universal):
        for i in universal:
            if i not in self.conjunto:
                self.conjunto.append(i)
        return self.conjunto

    def imprimir(self):
        return self.conjunto

def merge_the_tools(string, k):
    agrupados = [string[letra:k + letra] for letra in range(0, len(string), k)]
    resultado = []
    for i in range(len(agrupados)):
        C = Conjunto_disyunto()
        C.crea_conjunto(agrupados[i])
        resultado.append(C.imprimir())
    for i in resultado:
        print("".join(i))
    
merge_the_tools("AABCAAADA",3)
