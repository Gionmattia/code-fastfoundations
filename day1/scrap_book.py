string = "violet_blue|convert|red|6.3327|9.4423|113.3428|7.3298|5.3353|9.9283|over|all"
def from_string_to_list(inpts):
    my_list = inpts.split("|")
    coordinates = []
    for each in my_list:
        if each[0].isnumeric():
            coordinates.append(each)
    return coordinates

def tuplizer(coordinates):
    tup = []
    for each in range(0, int(len(coordinates)/2)):
        t = (float(coordinates[each]),float(coordinates[each+3]))
        tup.append(t)
    return tup

def dist(a,b):
    """
    Takes a list of points as input, returns the distance
    """
    d = (a-b)**2
    return d

def get_distance(tup):
    sum = 0
    for each in tup:
        sum = sum + dist(each[0],each[1])
    distance = sum**0.5
    return distance


tup = tuplizer((from_string_to_list(string)))
distance = get_distance(tup)
print(distance)