def direction(numbers):
    a = numbers[0]
    for i in range(1, len(numbers)):
        if a > numbers[i]:
            return "Не возраставет"
        else:
            a = numbers[i]
    return "Возрастает"
print(direction([1, 25, 37, 49, 55]))
print(direction([-10000000000, -198, 0, 198, 289, 298, -10000000000000000000000000000000000]))