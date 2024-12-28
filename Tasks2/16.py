def size (data):
    full_size = []
    for i in data:
        size = 1
        for j in i:
            size *= j
        full_size.append(size)
    res = 0
    for i in full_size:
        res += i
    return res
print(size([[1,5,25],[1,1,1],[2,7,5]]))