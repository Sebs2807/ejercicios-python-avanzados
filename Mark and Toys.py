def maximumToys(prices,k,n):
    prices.sort()
    suma = 0
    for i in range(n):
        suma += prices[i]
        if suma >= k:
            return prices[:i]
def main():
    n,k = map(int,input().split(" "))
    prices = list(map(int,input().split(" ")))
    print(len(maximumToys(prices,k,n)))
main()