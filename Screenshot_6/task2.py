def biggest_dict(*args):
    main = {'first_one':'we can do it'}
    temp = {}
    for par in args:
        vk = par.split(':',1)
        key = vk[0]
        value = vk[1]
        temp[key] = value
    main.update(temp)
    return main
print(biggest_dict('name:ivan', 'age:25'))