def to_dict(lst):
    dictionary = {}
    for name in lst:
        dictionary[name] = name
    return dictionary
print(to_dict(['cat','dog']))
