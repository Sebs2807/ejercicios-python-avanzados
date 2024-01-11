def largestPermutation(k,arr,n):
  if k >= n:
    arr.sort(reverse = True)
    return arr
  i = 0
  if k % 2 == 0:
    while i < k + 2:
        pos = arr.index(n - i)
        arr[i],arr[pos] = arr[pos],arr[i]
        i += 1
        k -= 1
  if k % 2 == 1:
    while i < k + 2:
        pos = arr.index(n - i)
        arr[i],arr[pos] = arr[pos],arr[i]
        i += 1
        k -= 1
  return arr
def main():
  n,k = map(int,input().split(" "))
  arr = list(map(int, input().rstrip().split()))
  print(largestPermutation(k,arr,n))
main()