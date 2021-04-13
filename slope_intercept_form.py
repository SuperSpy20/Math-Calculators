import math
try:
    xy = input('What coordinates are on the line?\n').split(',')
    slope = input('What is the slope of the line?\n')

    xy = list(xy)
    x1 = xy[0]
    y1 = xy[1]

    x1 = int(x1)
    y1 = int(y1)

    slope = int(slope)
except:
    print('\n\nYou must input a correct slope and correct coordinate!')
    exit()

def linear_equation(x1, y1, slope):
    
    if x1 < 0:
        x_operator = "+"
        x_abs = abs(x1)
    else:
        x_operator = "-"
        x_abs = x1
        
    if y1 < 0:
        y_operator = "+"
        y_abs = abs(y1)
    else:
        y_operator = "-"
        y_abs = y1
        
    
    # if slope < 0:
        # if x_operator == "-":
                # x_operator = "+"
    
    #First Linear Equation
    linear_equation = "\ny {} {} = {}(x {} {})  -->".format(y_operator, y_abs, slope, x_operator, x_abs)
    
    print(linear_equation)

    y_int = (slope) * (x_abs)
    
            
    if y_int > 0:
        if x_operator == "-":
            y_int = int("-{}".format(y_int))
            y_int_space = abs(y_int)
            
    if slope < 0:
        if x_operator == "-":
            if y_int < 0:
                y_int = abs(y_int)
                x_operator = "+"

    if y_int < 0:
        if x_operator == "+":
            x_operator = "-"
            y_int_space = abs(y_int)
            
    #Stating that if a minus sign is next to a negative, then remove print the absolute value of the number
    if y_int < 0:
        if x_operator == "-":
            y_int_space = abs(y_int)
            
    #Second Linear Equation
    linear_equation = "y {} {} = {}x {} {}  -->".format(y_operator, y_abs, slope, x_operator, y_int)
    
    if y_int < 0:
        if x_operator == "-":
            linear_equation = "y {} {} = {}x {} {}  -->".format(y_operator, y_abs, slope, x_operator, y_int_space)
            
    
    print(linear_equation)
    
    y_int_final = (y1) + (y_int)
        
    y_int_space = abs(y_int_final)
        
    #Third Linear Equation
    linear_equation = "y = {}x {} {}".format(slope, x_operator, y_int_space)
    
    if y_int_final > 0:
        if x_operator == "-":
            linear_equation = "y = {}x {} {}".format(slope, x_operator, y_int_space)
    
    
    
    return linear_equation
    
line = linear_equation(x1,y1,slope)
print("\nLinear Equation: {}".format(line))
