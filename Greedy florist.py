def getMinimumCost(k,c,n):
    c.sort(reverse = True)
    suma = 0
    cont = 0
    for i in range(0,n,k):
        try:
            for j in range(i,i + k):
                suma += c[j] * (cont + 1)
            cont += 1
        except:
            return suma
    return suma
def main():
    n,k = map(int,input().split(" "))
    c = list(map(int, input().rstrip().split()))
    print(getMinimumCost(k,c,n))
main()