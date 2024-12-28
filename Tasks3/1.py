def rps(p1,p2):
    p1.lower()
    p2.lower()
    r = "к"
    p = "б"
    s = "н"
    w1 = "Выйграл первый"
    w2 = "Выйграл второй"
    if p1 == p2:
        return "Ничья"
    if p1 == s and p2 == p:
        return w1
    elif p1 == p and p2 == r:
        return w1
    elif p1 == r and p2 == s:
        return w1
    elif p2 == r and p1 == s:
        return w2
    elif p2 == p and p1 == r:
        return w2
    elif p2 == s and p1 == p:
        return w2
a = str(input("Первый игрок: "))
b = str(input("Второй игрой: "))
print(rps(a,b))
