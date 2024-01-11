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

def marble():
    cola = ColaDePrioridad()
    n,q = input().split(" ")
    for _ in range(int(n)):
        cola.push(input())
    print(cola.imprimir())
marble()