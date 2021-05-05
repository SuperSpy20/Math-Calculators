import math

def correl_coeff(x, y):
    # finding the sum of each x and y list
    x_sum = sum(x)
    y_sum = sum(y)

    xy = []
    # mutliplying each element in the set by the other
    
    for z, i in zip(x, y):
        p = (z)*(i)
        xy.append(p)
    
    # finds the sum of the mutlitplication
    xy_sum = sum(xy)
    
    # this whole part finds the top part of the formula (https://athensrc.owschools.com/media/g_alg01_ccss_2016/11/g_alg01u11l19_example01.gif)
    xy_sum = (xy_sum)*(len(x))
    
    x_sum_y_sum = (x_sum)*(y_sum)
    
    
    top = (xy_sum)-(x_sum_y_sum)
    
    
    # finding the squared version of each element in the sets
    x_sq = []
    for z, i in enumerate(x):
        p = math.pow(i, 2)
        if str(p).endswith(".0"):
            p = int(p)
        x_sq.append(p)
    
    y_sq = []
    for z, i in enumerate(y):
        p = math.pow(i, 2)
        if str(p).endswith(".0"):
            p = int(p)
        y_sq.append(p)
    
    # create the left bottom section of the formula in the link above
    left_bott_1 = (len(x))*(sum(x_sq))-(math.pow(sum(x), 2))
    left_bott = math.sqrt(left_bott_1)
    
    if str(left_bott).endswith(".0"):
        left_bott = int(left_bott)
    
    # do the same with the right bottom section of the formula
    right_bott_1 = (len(y))*(sum(y_sq))-(math.pow(sum(y), 2))
    right_bott = math.sqrt(right_bott_1)
    
    if str(right_bott).endswith(".0"):
        right_bott = int(right_bott)
    
    bottom = (left_bott)*(right_bott)
    
    correlation_coeff = round((top)/(bottom), 3)
    
    print(correlation_coeff)
# grabs the user's x set    
x = input("What is the first set (x)?\n").split(",")

# check that each element in the set is a number
try:
    for z, i in enumerate(x):
        x[z] = float(i)
        
        # turns the number into a whole number if it ends with .0
        if str(x[z]).endswith(".0"):
            x[z] = int(i)
except:
    print("\n\nYou must supply a set of numbers!")

# grabs the user's y set
y = input("What is the second set (y)?\n").split(",")

# does the same, check that each element in the set is a number
try:
    for z, i in enumerate(y):
        y[z] = float(i)
        
        # turns the number into a whole number if it ends with .0
        if str(y[z]).endswith(".0"):
            y[z] = int(i)
except:
    print("\n\nYou must supply a set of numbers!")

# calls the function
correl_coeff(x, y)
