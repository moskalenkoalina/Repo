 n = int(input())
result = []
i = 1
while len(result) < n:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        result.append(i)
    i += 1
print(" ".join(map(str, result)))
