# Пользователь вводит N (N > 2), а затем список из N чисел.
# Найдите два наибольших числа в этом списке.

ch = int(input('ведите число: '))

list = []
listMax = []

i = 0

if ch > 2:
    while True:

        if i != ch:
            ch2 = int(input('Введите числа: '))
            i += 1
            list.append(ch2)

        else:
            break
else:
    print("Число меньше заданного условия")

if len(list) != 0:
    print(max(list))
    listMax.append(max(list))
    list.remove(max(list))
    listMax.append(max(list))
    listMax.sort()
    print(listMax)
else:
    print('Лист пустой')



