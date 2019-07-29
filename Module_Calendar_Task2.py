# Пользователь вводит название дня недели.
# Вывести ближайший месяц и год, когда этот день недели выпадал на 1-ое число.

import calendar

bd = input('Введите день недели: ')
mon = 7
year = 2019

listMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']

listDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i, n in enumerate(listDay):
    if bd == n:
        while True:
            mon += 1

            if mon == 13:
                year = year + 1
                mon = 0



            elif i in calendar.monthrange(year, mon):
                print(listDay[i])
                print(str(listMonth[mon]) + ' ' + str(year))
                break
