def delete_name(people,enemies):
    new = []
    for enemy in enemies:
        for i in range (0,len(people)-1):
            if people[i] != enemy and people[i] not in new :
                new.append(people[i])
    return new
print(delete_name(['dog','cat','skeleton'], ['boo', 'skeleton']))