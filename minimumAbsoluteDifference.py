def minimumAbsoluteDifference(lista, longitud):
    lista.sort()
    menor = abs(lista[0] - lista[1])
    for i in range(1, longitud):
        diferencia = abs(lista[i] - lista[i - 1])
        if diferencia < menor:
            menor = diferencia
    return menor 
def main():
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr,n)
    print(str(result) + '\n')
main()