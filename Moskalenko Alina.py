import os
def quadratic(input_file, output_file):
    if not os.path.exists(input_file):
        print("Файл не знайдено")
        return

def quadratic_d(a,b,c):
    if a == 0:
        return None
    diskriminant = b ** 2 - 4 * a * c
    if diskriminant > 0:
        k_1 = (-b - (diskriminant ** 0,5)) / 2 * a
        k_2 = (-b + (diskriminant ** 0,5)) / 2 * a
        return k_1,k_2
    if diskriminant == 0:
        k = -b / 2 * a
    else:
        return "Коренів немає"


def process_file(input_file, output_file):
    results = []
    with open(input_file, "r") as file:
        for line in file:
            try:
                a, b, c = map(float, line.split())
                result = quadratic_d(a, b, c)
                results.append(result)
            except ValueError:
                print("Неправильні дані ")
process_file(input_file, output_file)