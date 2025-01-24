 from math import factorial

 def C1(n,k):
     return factorial(n) // factorial(k) // factorial(n - k)

 def print_pascal(n):
     for i in range(n):
         for j in range(i + 1):
             print(C1(i,j), end=" ")
print_pascal(10)