def to_float(num):
    if type(num) != int:
        print ('Невозмоно преобразовать')
    else:
        num = float(num)
        return num
print(to_float(525))
