class ColaDePrioridad:
    def __init__(self):
        self.cola = [] 
    
    def push(self,prioridad,nombre):
        tupla = (prioridad,nombre)
        dentro = False
        for i,(p,_) in enumerate(self.cola):
            if prioridad < p:
                self.cola.insert(i,tupla)
                dentro = True
                break
            
        if not dentro:
            self.cola.append(tupla)
    def pop(self):
        if not self.vacio():
            x = self.cola[0]
            del self.cola[0]
            return x
        
    def vacio(self):
        return len(self.cola) == 0

    def imprimir(self):
        return self.cola

def minimumAverage(customers,n):
    cola = ColaDePrioridad()
    for i in range(len(customers)):
        cola.push(customers[i][1],customers[i][0])
    nueva = []
    resta = 0
    for i,j in cola.imprimir():
        resta = j - resta
        nueva.append((i,j,resta))
    promedio = 0
    final = 0
    for p,l,r in nueva:
        promedio += p - r
        final += promedio
    return final // n

def main():
    n = int(input())
    customers = []
    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))
    print(minimumAverage(customers,n))
main()