import math
def equation(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    D = (b * b) - 4 * a * c
    D = math.sqrt(D)
    if D > 0:
        x1 = (-b + D) / (a * 2)
        x2 = (-b - D) / (a * 2)
        return x1, x2
    elif D == 0:
        x = -b / (a * 2)
        return x
    else:
        return 'корней нет'


a = 4
b = -3
c = 3
print(equation(a, b, c))
