def extraLongFactorials(n):
    if n <= 1:
        return(n)
    else:
        return(n * extraLongFactorials(n - 1))
def main():
    n = int(input().strip())
    print(extraLongFactorials(n))
main()