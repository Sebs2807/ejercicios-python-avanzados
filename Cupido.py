def heights(n1,princess,altura):
  princess.sort()
  for i in range(n1):
    if i != 0:
      if princess[i] >= altura:
        return princess[i - 1]
    else:
      if princess[i] >= altura:
        return -1
def main():
  n1 = int(input())
  princess = list(map(int,input().split(" ")))
  n2 = int(input())
  prince = list(map(int,input().split(" ")))
  for i in range(n2):
    altura = prince[i]
    final = heights(n1,princess,altura)
    if final == -1:
      print("X")
    else:
      print(final)
main()