s = input('Введите выражение: ')

tokens = []


def Multiplication():
    tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
    del tokens[index:index + 2]


def Division():
    tokens[index2 - 1] = tokens[index2 - 1] / tokens[index2 + 1]
    del tokens[index2:index2 + 2]


def Plus():
    tokens[index3 - 1] = tokens[index3 - 1] + tokens[index3 + 1]
    del tokens[index3:index3 + 2]


def Minus():
    tokens[index3 - 1] = tokens[index3 - 1] - tokens[index3 + 1]
    del tokens[index3:index3 + 2]


while True:
    for i, ch in enumerate(s):
        if ch in ('+', '-', '*', '/'):
            tokens.append(float(s[:i]))
            tokens.append(s[i])
            s = s[i + 1:]
            break
    else:
        tokens.append(float(s))
        break

while True:
    for index, cha in enumerate(tokens):
        if cha == '*':
            Multiplication()
            if cha == '*':
                Multiplication()

    break

while True:
    for index2, cha2 in enumerate(tokens):
        if cha2 == "/":
            Division()
            if cha2 == "/":
                Division()
    break

for index3, cha3 in enumerate(tokens):
    if cha3 == '+':
        Plus()
        if cha3 == '+':
            Plus()

        if cha == '-':
            Minus()
            if cha == '-':
                Minus()

print(*tokens)
