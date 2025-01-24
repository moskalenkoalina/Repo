from array import array

n = int(input())
arr = [int(x) for x  in input().split()]
count = {}
for number in arr:
    count[number] = count.get(number, 0) + 1
majority_element = next((num for num, freq in count.items() if freq > n // 2), -1)

print(majority_element)


