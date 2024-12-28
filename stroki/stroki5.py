def shortener(st):
    deleter = False
    word = ""
    for i in st:
        if i == "(":
            deleter = True
        elif i == ")":
            deleter = False
        elif not deleter:
            word += i
    return word.strip()
print(shortener("Коты очень мягкие и пушистые, они любят ласку(не всегда)."))