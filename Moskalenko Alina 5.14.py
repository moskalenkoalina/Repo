n, k = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()
N = lst[k-1]
print(N)