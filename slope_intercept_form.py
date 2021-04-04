try:
    slope_int_input = input('What is the coordinate that lies on the line?\n').split(',')
    slope_input = input('What is the slope of the line?\n')

    p = list(slope_int_input)
    x1 = p[0]
    y1 = p[1]

    x1 = int(x1)
    y1 = int(y1)

    q = int(slope_input)
except:
    print('\n\nYou must enter a proper coordinate and slope!')
    exit()

def slope_intercept(x1, y1, slope):

    if slope == 0:
        print('\n\nThe slope must not be zero!')
        exit()

    linear_0 = "y - {} = {}(x - {})   -->".format(y1, slope, x1)
    if y1 < 0:
        y2 = "{}".format(y1)
        y3 = y2.strip('-')
    else:
        y3 = y1
     
        linear_0 = "y + {} = {}(x - {})   -->".format(y3, slope, x1)
    if x1 < 0:
        x2 = "{}".format(x1)
        x3 = x2.strip('-')
        
        linear_0 = "y + {} = {}(x + {})   -->".format(y3, slope, x3)
    
    print(linear_0)
    
    y_int = (slope)*(x1)
    
    linear_1 = "y - {} = {}x - {}   -->".format(y3, slope, y_int)
    if y1 < 0:
        linear_1 = "y + {} = {}x - {}   -->".format(y3, slope, y_int)
    
    print(linear_1)
    
    y_int_final = (y1)-(y_int)
    
    linear_2 = "\ny = {}x {}".format(slope, y_int_final)

    if y_int_final > 0:
        linear_2 = "\n\ny = {}x + {}".format(slope, y_int_final)
    
    return linear_2
    
    
    

slope_calculation = slope_intercept(x1, y1, q)

print('\n\nYour Linear Equation: %s'%slope_calculation)