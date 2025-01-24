n = int(input())
cub = input()
count = {}
for i in cub:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for letter, q in count.items():
    if q % 2 != 0:
        print(letter)
        break
else:
    print("Ok")
