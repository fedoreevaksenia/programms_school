def lst_sort(lst):
    for i in range(len(lst)):
        for i in range (len(lst)-1):
            if lst[i]>lst[i+1]:
                lst [i],lst[i+1]=lst[i+1],lst[i]
    return lst
print(lst_sort([1996,525,2008,-1001,-922]))