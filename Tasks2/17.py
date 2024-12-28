import math
def round(number):
    factor = 10 ** 3
    integer_part = int(number * factor)
    fractional_part = number * factor - integer_part
    if fractional_part >= 0.5:
        integer_part += 1
    return integer_part / factor
def pyphagor(dict):
    x = dict.get('x')[0] - dict.get('x')[1]
    y = dict.get('y')[0] - dict.get('y')[1]
    length = math.sqrt(x**2 + y**2)
    length = round(length)
    return length
print(pyphagor({'x':[2,9],
            'y':[2,5]}))