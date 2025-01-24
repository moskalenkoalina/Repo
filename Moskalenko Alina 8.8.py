def fast(n):
    binary_n = bin(n)[2:]
    rule = []
    for bit in binary_n:
        if bit == '1':
            rule.append('SX')
        else:
            rule.append('S')
    return ''.join(rule[1:])

n = int(input())
print(fast(n))
