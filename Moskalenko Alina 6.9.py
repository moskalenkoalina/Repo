n = input()
count = 0
i = 0

while i < len(n):
    if n[i:i+2] == '**' or n[i:i+2] == '//':
        count += 1
        i += 2
    elif n[i] in ['+','-','*','/','%',]:
        count += 1
        i += 1
    else:
        i += 1
print(count)