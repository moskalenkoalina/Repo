def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def count_pairs(A, B):
    if B % A != 0:
        return 0

    k = B // A
    count = 0
    for p in range(1, int(k ** 0.5) + 1):
        if k % p == 0:
            q = k // p
            if gcd(p, q) == 1:
                count += 2 if p != q else 1

    return count


A, B = map(int, input().split())
print(count_pairs(A, B))