def passer(st):
    sum = 0
    special_symbol = False
    capital_symbol = False
    digit = False
    lower_symbol = False
    length = False
    for i in st:
        if not i.isalpha() and not i.isdigit():
            special_symbol = True
        if i.isupper():
            capital_symbol = True
        if i.islower():
            lower_symbol = True
        if i.isdigit():
            digit = True
    if len(st) >= 16:
        length = True
    sum = special_symbol + capital_symbol + digit + lower_symbol + length
    return f"Сложность пароля: {sum}"
print(passer('abcXYZ59153320LOKboo'))
print(passer('Abcd1234'))