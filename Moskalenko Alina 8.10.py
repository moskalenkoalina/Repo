def f(a, b):
    if len(b) == len(a):
        print(*b)
        return
    for i in range(len(a)):
        if a[i] not in b:
            f(a, b + [a[i]])

n = int(input())
a = list(range(1, n + 1))
print(f(a, []))
