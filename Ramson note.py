class Hash:
    def __init__(self):
        self.dict = [0] * 1000

    def insertar(self,palabra):
        diccionario = self.diccionario()
        clave = self.cifrador(palabra,diccionario)
        if self.dict[clave] == 0:
            self.dict[clave] = [palabra]
        else:
            self.dict[clave].append(palabra)
    
    def eliminar(self,palabra):
        valido = True
        diccionario = self.diccionario()
        clave = self.cifrador(palabra,diccionario)
        if self.dict[clave] == []:
            valido = False
        else:
            try:
                del self.dict[clave][-1]
            except:
                valido = False
                return valido  
        return valido
     
    def diccionario(self): 
        letras_ingles = {}

        for i, letra in enumerate(range(ord('a'), ord('z') + 1), start=1):
            letras_ingles[chr(letra)] = i

        for i, letra in enumerate(range(ord('A'), ord('Z') + 1), start=len(letras_ingles) + 1):
            letras_ingles[chr(letra)] = i
            
        return letras_ingles
    
    def cifrador(self,palabra,diccionario):
        suma = 0
        for letra in palabra:
            if letra in diccionario:
                suma += diccionario[letra]
            else:
                print("La letra no está en el idioma inglés")
        return suma - 1
    
    def imprimir(self):
        return self.dict

        
def checkMagazine(magazine,note,m,n):
    valido = True
    if n > m:
        valido = False
    H = Hash()
    #Agregar las palabras de la revista
    for i in magazine:
        H.insertar(i)
    #Quitamos palabras de la revista cuando las usamos en la nota
    for j in note:
        if not H.eliminar(j):
            valido = False
            break
    
    if valido:
        print("Yes")
    else:
        print("No")
    
checkMagazine(["two","times","three","is","not","four"],["two","times","two","is","four"],6,5)
    