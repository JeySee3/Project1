# Пользователь вводит N, а затем список из N чисел.
# Если среди элементов есть нули, переместите их в
# начало списка (оставшиеся элементы должны остаться в исходном порядке),
# и выведите на экран получившийся список
ch = int(input('ведите число: '))

listMy = []

i = 0
k = 0

while True:

    if i != ch:
        ch2 = int(input('Введите числа: '))
        i += 1
        listMy.append(ch2)

    else:
        break

print(listMy)

if k in listMy:
    for r, zero in enumerate(listMy):
        if zero == 0:
            listMy.insert(k, zero)
            del listMy[r + 1]

print(listMy)
