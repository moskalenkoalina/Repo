def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm1(n):
    lcm_result = 1
    for i in range(2, n + 1):
        lcm_result = lcm(lcm_result, i)
    return lcm_result

n = int(input())
print(lcm1(n))