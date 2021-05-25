import math
from class_geometry import Geometry

def three_dimen_slope_int(slope, y_int, x_int, z_int):
    
    # this finds the y value of the x intercept
    y = (x_int)*(slope)
    
    # int checks it
    if str(y).endswith(".0"):
        y = int(y)

    # this finds the x, y, and z values of the 3 dimensional coordinates of the x intercept
    print("\n(In 3 Dimensional Coordinates (x, y, z))")
    print("X-Intercept: ({}, {}, {})".format(x_int, y, 0))
    
    # this does the same with the z intercept
    print("Z-Intercept: ({}, {}, {})".format(0, y_int, z_int))
    
    

## main
print("What're two points on the line (Facing the x-axis)")

# gathers the two points
x = input("\n1st Point:\n")
y = input("\n2nd Point:\n")

# splits them into lists separated by commas
try:
    x = x.split(",")
    y = y.split(",")
except:
    print("\n\nThe points' x and y values must be separated by a comma!")
    exit()

# creates a function that makes each number a decimal, and if it ends with .0, the number is a whole number
def int_check(x):
    #try:
    for z, i in enumerate(x):
        x[z] = float(i)
        
        if str(x[z]).endswith(".0"):
            x[z] = int(x[z])
    #except:
        # print("\n\nThe points must be numbers!")
        # exit()

# calls the function for both lists
int_check(x)
int_check(y)

# this uses a function from another file that solves for the slope
slope = Geometry.slope(x, y)
# slope doesn't need to be int checked because it will not be printed/visible to the user

x1 = x[0]
y1 = x[1]

# this finds the y-intercept of the slope intercept form. this is used later
y_int = Geometry.slope_intercept(x1, y1, slope)

# int checks it
if str(y_int).endswith(".0"):
    y_int = int(y_int)


# this gathers the user's input for the x and z intercept
x_int = input("\n\nWhat is the x value of the x-intercept?\n")
z_int = input("\nWhat is the z value of the z-intercept?\n")


# this is a modified version of the 'int_check()' function for the x and z intercepts
def int_check_intercept(x):
    try:
        x = float(x)
        
        if str(x).endswith(".0"):
            x = int(x)
    except:
        print("\n\nThe x and z-intercepts must be numbers!")
        exit()
    return x

# this calls the int_check_intercept() function

x_int = int_check_intercept(x_int)
z_int = int_check_intercept(z_int)



# calls the function 
three_dimen_slope_int(slope, y_int, x_int, z_int)