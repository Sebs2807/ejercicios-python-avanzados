class Hash:
    def __init__(self):
        self.dict = [[]] * (11)

    def insertar(self, clave, valor):
        self.dict[clave] = [valor]

    def eliminar(self, palabra):
        diccionario = self.diccionario()
        clave = self.cifrador(palabra, diccionario)

        if self.dict[clave] == []:
            print(f"No hay valores para eliminar en la posición {clave}.")
        else:
            del self.dict[clave][-1]

    def imprimir(self):
        return self.dict

    def operacion(self):
        for i in range(2, 11):
            cases = self.dict[i][0]
            primes = self.dict[i - 1][0]

            if cases > primes + 1:
                self.insertar(i,primes + 1) 
                cases = self.dict[i][0]

            for j in range(2, i + 1):
                divisors = i * j

                if divisors >= 10:
                    break

                value = self.dict[divisors][0]

                if value > cases + 1:
                    self.insertar(divisors,cases + 1)

def downToZero(n):
    H = Hash()
    for i in range(0,11):
        H.insertar(i, i)
    if n <= 3:
        print(n)
    else:
        H.operacion()
        print(H.imprimir()[n][0])
downToZero(3)