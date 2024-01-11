def toys(w,n):
    matriz = []
    w.sort()
    inicio = 0
    k = 0
    i = 0
    while i < n:
        if w[i] <= w[inicio] + 4:
            k += 1
            if i == n - 1:
                matriz.append(w[inicio:])
        else:
            matriz.append(w[inicio:inicio + k])
            inicio += k
            i = inicio - 1 
            k = 0
        i += 1
    return matriz
def main():
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    print(len(toys(w,n)))
main()