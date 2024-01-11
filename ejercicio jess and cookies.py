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
    
def cookies(k,cola):
    cont = 0
    while not all(i >= k for i in cola.imprimir()):
        try:
            cola.push(cola.pop() + 2 * (cola.pop()))
            cont += 1
        except:
            cont = -1
            return cont
    return cont

if __name__ == '__main__':
    
    cola = ColaDePrioridad()

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    for i in A:
        cola.push(i)
    
    print(cookies(k,cola))
    




