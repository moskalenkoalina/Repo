n=int(input())
k=1
i=2
while i<=(n//2):
    if n%i==0:
        k=(n//i)
        break
    else:
        i=i+1
print(k)
