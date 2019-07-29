from math import acos, degrees


print("Введите длинны сторон предполагаемого треугольника: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    cosA1 = degrees(acos((a * a + c * c - b * b) / (2.0 * a * c)))
    cosB1 = degrees(acos((a * a + b * b - c * c) / (2.0 * a * b)))
    cosY1 = degrees(acos((b * b + c * c - a * a) / (2.0 * c * b)))


    print('α = ' + str(round(cosA1)))
    print('β = ' + str(round(cosB1)))
    print('γ = ' + str(round(cosY1)))
else:
    print("Треугольник не существует")
