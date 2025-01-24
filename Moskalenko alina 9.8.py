n = int(input())
q = list(map(int,input().split()))
mods = set()
for i in q:
    mods.add(abs(i))
print(len(mods))