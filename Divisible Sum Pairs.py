def divisibleSumPairs(n, k, ar):
    cant=0
    for i in range(n):
        for j in range(i):
            if (ar[i]+ar[j])%k==0:
                cant+=1
    return(cant)
def main():
    n,k = input().split(" ")
    ar = list(map(int, input().rstrip().split()))
    print(divisibleSumPairs(n, k, ar))
main()