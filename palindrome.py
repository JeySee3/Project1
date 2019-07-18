text = input('')

if text == ''.join(reversed(text)):
    print("It's palindrome")
else:
    print("It's not palindrome")
