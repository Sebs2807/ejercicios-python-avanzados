def maxMin(k,arr,n):
    arr.sort()
    menor = arr[k - 1] - arr[0]
    for i in range(1,(n - k) + 1):
        aux = arr[k + (i -1)] - arr[i]
        if menor > aux:
            menor = aux
    return menor 
def main():
    n = int(input())
    k = int(input())
    cont = 0
    lista = []
    while cont < n:
        cont += 1
        lista.append(int(input()))
    print(maxMin(k,lista,n))
main()