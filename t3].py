def pascal_value(n, k):
    if k == 0 or k == n:
        return 1
    return pascal_value(n - 1, k - 1) + pascal_value(n - 1, k)

def pascal_val(p):
    for i in range(p):
        row = [pascal_value(i, k ) for k in range(i + 1)]
        print(row)

p = 10
pascal_val(p)