import random

ch = random.randrange(10)


while True:
    number = int(input('Угадайте число от 1-10: '))
    if number == ch:
        print('Вы угадали!')
        break
    else:
        print('Попробуй еще раз :(')
