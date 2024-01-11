def trib(n,back):
    global cont
    cont = cont + 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    acum = 0
    for i in range(1,back + 1):
        acum = acum + trib(n - i,back)
    return acum

def main():
    resultado = []
    while True:
        n,back = [int(x) for x in input().split()]
        if n == 61 and back == 61:
            break
        global cont
        cont = 0
        trib(n,back)
        resultado.append(cont)
    for i,_ in enumerate(resultado):
        print(f"Case {i + 1}: {_}")
main()