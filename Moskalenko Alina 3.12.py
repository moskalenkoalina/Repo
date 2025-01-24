m = int(input())
l = 0

while str(m) != str(m)[::-1]:
    m += int(str(m)[::-1])
    l += 1

print(l)