def ordenamiento(total,clientes):
  for i in range(1,len(total)):
    insertar = total[i]
    insertar2 = clientes[i]
    indice = i 
    while indice > 0 and total[indice - 1] > insertar:
      total[indice] = total[indice - 1]
      clientes[indice] = clientes[indice - 1]
      indice -= 1
    total[indice] = insertar
    clientes[indice] = insertar2 
  return clientes
def sumatorias(atencion,orden,clientes): 
  total = [] 
  for i in range(len(clientes)): 
    total.append(int(atencion[i]) + int(orden[i])) 
  clientes = ordenamiento(total,clientes)
  return clientes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    cclientes = int(input().strip()) 
    clientes = [] 
    for i in range(cclientes):  
      clientes.append(i + 1) 
    contador = 0  
    atencion = [] 
    orden = []  
    while contador < cclientes:
        entrada = input().strip()
        atencion.append(entrada.split(" ")[0]) 
        orden.append(entrada.split(" ")[1])
        contador += 1
    final = sumatorias(atencion,orden,clientes) 
    fptr.write(' '.join(map(str, final)))
    fptr.write('\n')
fptr.close()