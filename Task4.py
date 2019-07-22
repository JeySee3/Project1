# Пользователь вводит x и N. Посчитайте приблизительное значение
# cos(x) с точностью до N-ого члена его разложения:
from math import factorial

x = int(input('Введите x: '))
n = int(input('Введите n: '))

listMy = []

for nr in range(1, n):  # Берем количество рядов
    listMy.append(nr)
listMy.append(n)

newList = []

for ex in listMy:
    n1 = float((-1) ** ex)
    n2 = float(x ** (2 * ex))
    n3 = float(factorial(2 * ex))
    fullEx = n1 * n2 / n3
    newList.append(float(fullEx))

it = sum(newList)
print(round((1+it), 4))
