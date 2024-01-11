class ColaDePrioridad:
    def __init__(self):
        self.cola = [] 
    
    def push(self,prioridad):
        dentro = False
        
        for i,p in enumerate(self.cola):
            if prioridad < p:
                self.cola.insert(i,prioridad)
                dentro = True
                break
            
        if not dentro:
            self.cola.append(prioridad)
    def pop(self):
        if not self.vacio():
            x = self.cola[0]
            del self.cola[0]
            return x
        
    def vacio(self):
        return len(self.cola) == 0

    def imprimir(self):
        return self.cola

def solve(arreglo,queries):
    retorno = []
    for i in range(len(queries)):
        retorno.append(operacion(arreglo,queries[i]))
    return retorno
def operacion(arr,agrupar):
    cola = ColaDePrioridad()
    lista2 = []
    for i in range(0,(len(arr) - agrupar) + 1):
        final = (i + agrupar)
        lista2.append(arr[i:final])
    for i in lista2:
        cola.push(max(i))
        
    return cola.pop()
      
print(solve([33,11,44,11,55],[1,2,3,4,5]))


