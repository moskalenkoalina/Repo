import math


def triangle_area(a, b, c):
    assert a > 0 and b > 0 and c > 0
    assert a + b > c and a + c > b and b + c > a


    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

a = int(input())
b = int(input())
c = int(input())

print(f"Площа трикутника: {triangle_area(a, b, c)}")

