def revisador(n,A,B,k):
    bandera = True
    for i in range(n):
        if A[i] + B[i] < k:
            bandera = False
            return bandera
    return bandera
def permutador(n,k,A,B):
    A.sort(reverse = True)
    B.sort()
    if revisador(n,A,B,k):
        bandera = True
        return bandera
    else:
        bandera = False
        return bandera               
def main():
    queries = int(input())
    cont = 0
    answers = []
    while cont < queries:
        cont += 1
        n,k = input().split(" ")
        n,k = int(n),int(k)
        A = list(map(int,input().split(" ")))
        B = list(map(int,input().split(" ")))
        answers.append(permutador(n,k,A,B))
    for i in range(queries):
        if answers[i]:
            print("YES")
        else:
            print("NO")
main()

