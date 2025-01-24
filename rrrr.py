n = int(input())
array = [int(x) for x in input().split()]
count = {}
for x in array:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for x in array:
    if count[x] == 1:
        print(x,end=" ")