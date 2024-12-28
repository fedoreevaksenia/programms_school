def coordinates (x,y):
    coordinate = []
    for i in range (len(x)):
        coordinate.append(f"({x[i]};{y[i]})")
    return coordinate
print(coordinates([0,2,1,25], [0,4,1,625]))