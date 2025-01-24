def f(n):
    digits = "0123456789ABC"
    if n < 13:
        return digits[n]
    return f(n // 13) + digits[n % 13]

n = int(input())
print(f(n))