def unique_digit_numbers(a, b):
    result = []
    for number in range(a, b + 1):
        str_number = str(number)
        if len(set(str_number)) == len(str_number):
            result.append(str_number)
    return " ".join(result)

a, b = map(int, input().split())
print(unique_digit_numbers(a, b))