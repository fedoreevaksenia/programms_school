def reverser(a, b = []):
    length = len(a)
    for i in range(length - 1, -1, -1):
        b.append(a[i])
    return b
print(reverser([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
