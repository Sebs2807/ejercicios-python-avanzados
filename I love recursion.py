def formingMagicSquare(s):
    s = sum(s,[])
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    minimumcost = 10000000000
    for mag in magic:
        diff = 0
        for i,j in zip(s,mag):
            diff += abs(i - j)
        minimumcost = min(minimumcost,diff)
    return minimumcost
def main():
    matriz = []
    matriz.append(input().split())
    matriz.append(input().split())
    matriz.append(input().split())
    matriz = list(map(int,formingMagicSquare(matriz)))
    print(formingMagicSquare(matriz))
main()