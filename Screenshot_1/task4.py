def useless (lst):
    temp = lst [0]
    for i in (0,len(lst)-1):
        if temp < lst[i]:
            temp = lst[i]
    temp = temp / len(lst)
    return temp
print(useless([12345,525,798,6543]))
