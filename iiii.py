n = int(input())
array = [int(x) for x in input().split()]
counter = {}
for x in counter:
    if x in counter:
        counter[x] += 1
    else:
        counter[x] = 1

lst = []
for x in reversed(array):
    if counter[x] > 1:
        lst.append(x)
        counter[x] = 0
if lst:
    print(*reversed(lst))
else:
    print("No")