names = {'name1':'Vladislav',
        'name2':'Nick',
        'name3':'Deacon',
        'name4':'Viago',
        'name5':'Petyr',
        }
def dicter(dictionary):
    keys = list(dictionary.keys())
    dictionary[keys[0]], dictionary[keys[-1]] = dictionary[keys[-1]], dictionary[keys[0]]
    del dictionary[keys[1]]
    dictionary['new key'] = 'new value'
    return dictionary
print (dicter(names))