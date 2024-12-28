def massiv(*args):
    result = []
    temp = 0
    for num in args:
        for i in range(0, len(result)):
            temp += result[i]
        temp += num
        result.append(temp)
        temp = 0
    return result
print(massiv(1,2,3,4,5))