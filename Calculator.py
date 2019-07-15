s = input('Введите выражение: ')

tokens = []


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
            tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
            del tokens[index:index + 2]
    break

while True:
    for index2, cha2 in enumerate(tokens):
        if cha2 == "/":
            tokens[index2 - 1] = tokens[index2 - 1] / tokens[index2 + 1]
            del tokens[index2:index2 + 2]
    break

for index3, cha3 in enumerate(tokens):
    if cha3 == '+':
        tokens[index3 - 1] = tokens[index3 - 1] + tokens[index3 + 1]
        del tokens[index3:index3 + 2]

        if cha == '-':
            tokens[index - 1] = tokens[index3 - 1] - tokens[index3 + 1]
            del tokens[index3:index3 + 2]

print(*tokens)