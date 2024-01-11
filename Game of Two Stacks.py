def twoStacks(maxSum,a,b,ls1,ls2):
  maxnum = total = i = j = 0
  while i < ls1 and total + a[i] <= maxSum:
        total += a[i]
        i += 1
        maxnum += 1
  while j < ls2 and i >= 0:
        total += b[j]
        j += 1
        while i > 0 and total > maxSum:
            i -= 1
            total -= a[i]
        if total <= maxSum and maxnum < i + j:
            maxnum = i + j
  return maxnum
def main():
  consultas = int(input())
  cont = 0
  while cont < consultas:
    cont +=1
    ls1,ls2,maxSum = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(twoStacks(maxSum,a,b,ls1,ls2))
main()