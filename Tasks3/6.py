def time24_to_12 (time):
    hours = ""
    minutes = ""
    for i in range (0,2):
        hours += time[i]
    for i in range(3, 5):
        minutes += time[i]
    hours = int(hours)
    if hours > 12:
        hours = hours - 12
    else:
        hours = hours
    result = str(hours) + ":" + str(minutes)
    return result
def time12_to_24 (time, pm):
    hours = ""
    minutes = ""
    for i in range (0,2):
        hours += time[i]
    for i in range(3, 5):
        minutes += time[i]
    if pm:
        hours = int(hours) +12
    result = str(hours) + ":" + str(minutes)
    return result
def timer (st, type, pm = None):
    if type == "12":
        result = time12_to_24(st, pm)
    elif type == "24":
        result = time24_to_12(st)
    return result
print(timer("15:15", "24", pm = False))