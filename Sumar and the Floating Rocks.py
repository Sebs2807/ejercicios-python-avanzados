def encontrar_mcd(a, b):
    while b:
        a, b = b, a % b
    return a
def solve(x1,y1,x2,y2):
    contador = 0
    a,b = (y1 - y2),(x1 - x2)
    mcd = encontrar_mcd(a, b)
    Y,X = a // mcd,b // mcd
    while True:
        if Y < 0 or X < 0:
            if y1 < y2:
                x1 -= abs(X)
                y1 += abs(Y)
            if y1 > y2:
                y1 -= abs(Y)
                x1 += abs(X)
        if Y > 0 and X > 0:
            if y1 < y2:
                x1 += abs(X)
                y1 += abs(Y)
            if y1 > y2:
                y1 -= abs(Y)
                x1 -= abs(X)
        if X == 0:
            if y1 < y2:
                y1 += abs(Y)
            if y1 > y2:
                y1 -= abs(Y)
        if Y == 0:
            if x1 < x2:
                x1 += abs(X)
            if x1 > x2:
                x1 -= abs(X)
        if y1 == y2 and x1 == x2:
            return contador
        contador += 1
def main():
    cantidad = int(input())
    cont = 0
    final = []
    while cont < cantidad:
        cont += 1
        x1,y1,x2,y2 = map(int,input().split(" "))
        final.append(solve(x1,y1,x2,y2))
    for i in range(cantidad):
        print(final[i])
main()