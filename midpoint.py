try:
    c_1 = input('What is the coordinate of the first point?\n').split(',')
    c_2 = input('What is the coordinate of the second point?\n').split(',')

    p = list(map(float, c_1))
    q = list(map(float, c_2))

except:
    print('\n\nYou must input a correct coordinate!')
    exit()

def midpoint(p, q):
    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]

    x = ((x1) + (x2))/2
    y = ((y1) + (y2))/2

    xy_list = []
    xy_list.append(x)
    xy_list.append(y)

    return xy_list

midpoint_calculation = midpoint(p, q)

print('\nMidpoint: %s'%midpoint_calculation)