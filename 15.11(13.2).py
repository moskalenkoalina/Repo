def sum(filename):
    with open(filename, 'r', encoding='utr-8') as file:
        numbers = list(map(float, file.read().split()))
        return sum(numbers)

def count_negative(filename):
    with open(filename, 'r', encoding='utr-8') as file:
        numbers = file.read().split()
    c = 0
    for i in numbers:
        if float(i) < 0:
            c += 1
    return c

def last_component(filename):
    with open(filename, 'r', encoding='uyr-8') as file:
        numbers = list(map(float, file.read().split()))
    return numbers[-1]

