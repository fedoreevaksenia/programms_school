from typing import Any
def count_it(numbers):
    counter = {}
    for i in range (10):
        counter[i] = 0
    for number in numbers:
        counter[int(number)] += 1
    biggest = {}
    for i in range(3):
        max_num = -1
        big_key = None
        for number in counter:
            if int(counter[number]) > int(max_num):
                max_num = counter[number]
                big_key = number
        biggest[big_key] = max_num
        counter[big_key] = 0
    return biggest
print(count_it('525666131498171'))