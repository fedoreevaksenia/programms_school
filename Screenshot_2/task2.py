def rounder(number):
    factor = 10 ** 5
    integer_part = int(number * factor)
    fractional_part = number * factor - integer_part
    if fractional_part >= 0.5:
        integer_part += 1
    return integer_part / factor
def avg_5(a,b,c,d):
    avg = (a + b + c + d) / 4
    return rounder(avg)
print(avg_5(1.348979,10,100,525))