def coiner(coins):
    if (len(coins)) % 3 == 0:
        return True
    else:
        return False
print(coiner([252, 25, 25, 25, 50]))