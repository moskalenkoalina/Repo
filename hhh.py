def sum(filename):
    with open(filename, 'r', encoding='utr-8') as f:
        numbers = f.read.split()
        total = 0
        for i in numbers:
            total += i
        return total

def count_negative(filename):
    with open(filename, 'r', encoding='utr-8') as f:
        numbers = f.read().split()
         c = 0
        for i in numbers:
            if i < 0:
                c += 1
        return c

def last(filename):
    with open(filename, 'r', encoding='utr8') as f:
        numbers = list(map(float, file.read().split()))
    return numbers[-1]

def  largest(filename):
    with open(filename, 'r', encoding='utr8') as f:
        numbers = list(map(float, file.read().split()))
    return max(numbers)



