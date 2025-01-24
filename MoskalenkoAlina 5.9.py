# Читання вхідних даних
a, b, c, d = map(int, input().split())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

pro = set()

for i in range(a, b + 1):
    for j in range(c, d + 1):
        pro.add(i * j)

print(len(pro))