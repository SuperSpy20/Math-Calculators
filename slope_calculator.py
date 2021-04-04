c_1 = input('What is the first coordniate?\n').split(',')
c_2 = input('What is the second coordniate?\n').split(',')

p = list(map(float, c_1))
q = list(map(float, c_2))

def slope(coordinate_1, coordinate_2):
    x1 = coordinate_1[0]
    y1 = coordinate_1[1]
    x2 = coordinate_2[0]
    y2 = coordinate_2[1]


    try:
        m = (y2-y1)/(x2-x1)
    except:
        print('\n\nYou cannot divide by zero.')
        exit()
    return m

slope_calculation = slope(p, q)

print('\nSlope: %s'% slope_calculation)