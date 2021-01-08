n = int(input())
arr = list(map(int, input().split()))
if n==len(arr):
   print(max([x for x in arr if x!=max(arr)]))

    