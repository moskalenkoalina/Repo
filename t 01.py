def val(n,m):
    if m == 0 or n == 0 :
        return 0
    return val(n,m-1) + n

n = int(input())
m = int(input())
print(val(m,n))