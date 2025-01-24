
s = "a1b2c3d4"

sum_digits = 0

for char in s:
    if char.isdigit():
        sum_digits += int(char)

print("Сума цифр у рядку:", sum_digits)
