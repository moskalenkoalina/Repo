n = input()
count = 0

if any(z.islower() for z in n):
    count += 1
if any(z.isupper() for z in n):
    count += 1
if any(z.isdigit() for z in n):
    count += 1
if any(z in '!"#$%&\'()*+' for z in n):
    count += 1
if len(n) >= 8:
    count += 1

print(count)