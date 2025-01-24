s = 0
while True:
    i = int(input())
    if i == 0:
        break
    if i % 2 == 0:
        s += i
print(s)