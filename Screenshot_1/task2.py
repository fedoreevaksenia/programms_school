def change(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1], lst[0]
    return lst
print(change([525,1996,2008]))