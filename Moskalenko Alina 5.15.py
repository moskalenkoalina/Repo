n = int(input())

lst = list(map(int, input().split()))

max_element = max(lst)
min_element = min(lst)

res = []
for num in lst:
    if num == max_element:
        res.append(min_element)
    elif num == min_element:
        res.append(max_element)
    else:
        res.append(num)

print(" ".join(map(str, res)))