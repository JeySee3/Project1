# Пользователь вводит дату своего рождения в формате DD.MM.YYYY
# Вывести название дня недели, в который родился пользователь
import calendar

bd = input('Введите свою дату рождения в след. формате DD.MM.YYYY: ').split('.')
day = int(bd[0])
month = int(bd[1])
year = int(bd[2])

listDay = ["monday", "tue", "wed", "thu", "fri", "sat", "sun"]
print(listDay[calendar.weekday(year, month, day)])
