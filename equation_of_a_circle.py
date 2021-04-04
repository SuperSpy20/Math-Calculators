import math
try:
    center = input('What coordinates are the center of the circle?\n').split(',')
    radius = input('What is the radius of the circle?\n')

    center = list(center)
    x1 = center[0]
    y1 = center[1]

    x1 = int(x1)
    y1 = int(y1)

    radius = int(radius)
except:
    print('\n\nYou must input a correct center and radius of the circle!')
    exit()

def circle(x1, y1, radius):
    radius_squared = math.pow(radius, 2)
    
    radius_squared = round(radius_squared, 2)
    
    x = "x - {}".format(x1)
    y = "y - {}".format(y1)
    
    if x1 < 0:
        x3 = abs(x1)
        x = "x + {}".format(x3)
        
    if y1 < 0:
        x3 = abs(x1)
        y = "y + {}".format(y3)
    
    if x1 == 0:
        x = "x"
    if y1 == 0:
        y = "y"
    
    circular = "({})^2 + ({})^2 = {}".format(x, y, radius_squared)
    
    return circular
    
u = circle(x1, y1, radius)


print('\nYour equation is: %s'%u)