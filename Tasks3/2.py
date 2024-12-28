def silence(st):
    word = ""
    m = ""
    m_found = False
    for i in range(len(st)-1, -1, -1):
        if st[i] == "!" and not m_found:
            m = "!"
            m_found = True
        elif st[i] == "?" and not m_found:
            m = "?"
            m_found = True
        elif st[i] != "!" and st[i] != "?":
            word += st[i]
    word = word[::-1] + m
    return word
print(silence("BOO!!!!!!!!"))