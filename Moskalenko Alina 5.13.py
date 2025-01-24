n = int(input())
lst = list(map(float, input().split()))
res = 0
suma = 0

for i in lst:
    if i > 0:
        suma += i
        res += 1
if res > 0:
    print(f"{suma/res:.2f}")
else:
    print("Not Found")