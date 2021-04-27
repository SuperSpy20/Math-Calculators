import math

def law_of_cosines_ang(a,b,c):
    try:        
        def three_legs(a,b,c,leg_3,leg_2):
            def whole_num(q):
                if str(q).endswith(".0"):
                    q = int(q)
            
                    return q
                else:
                    pass
            
                    return q
            # whole_num states that if a decimal ends with .0, 
            # then turn it into a whole number so the calculations look alot nicer
            a = whole_num(a)
            b = whole_num(b)
            c = whole_num(c)
            
            # squares the legs squared and uses whole_num with it.
            c_sq = c ** 2
            b_sq = b ** 2
            a_sq = a ** 2
            
            c_sq = whole_num(c_sq)
            b_sq = whole_num(b_sq)
            a_sq = whole_num(a_sq)
            
            # solves the pythagorean theorem section of the theorem
            # and solves the 2ab section aswell
            first = (b_sq)+(a_sq)
            second = (2)*(a)*(b)
            
            first = whole_num(first)
            second = whole_num(second)
            
            # makes the second section negative because of the operator 
            second = float("-{}".format(second))
            second = whole_num(second)
            
            # subtracts the square root of c from both sides so we can get x by itself
            third = (c_sq)-(first)
            third = whole_num(third)
            
            
            # divides both sides to get x by itself
            fourth = (third)/(second)
            fourth = whole_num(fourth)
            
            # finds the degree measurement of x
            fourth = math.degrees(math.acos(fourth))
            angle_c = whole_num(fourth)
            
            # finds angle b with the law of sines
            sin = math.sin(math.radians(angle_c))
            ratio = (a)*(sin)
            sin_1 = (ratio)/(c)
            angle_b = math.degrees(math.asin(sin_1))
            
            # finds last angle again using law of sines
            sin = math.sin(math.radians(angle_c))
            ratio = (b)*(sin)
            sin_1 = (ratio)/(c)
            angle_a = math.degrees(math.asin(sin_1))
            
            # round the angles so they're more readable
            angle_a = round(angle_a, 2)
            angle_b = round(angle_b, 2)
            angle_c = round(angle_c, 2)
        
            # now that we've solved the whole triangle, were going to print it out for the user.
            print("\nLeg A: {}\nLeg B: {}\nLeg C: {}\n\nAngle A: {}°\nAngle B: {}°\nAngle C: {}°".format(a,b,c,angle_a,angle_b,angle_c))
        if leg_3 == True:        
            # call the function
            three_legs(a, b, c, leg_3, leg_2)
            # now let's do the 1 angle 2 leg calculator
        if leg_2 == True:
            # solves for the pythagorean theorem section of the equation.
            pythagorean_theorem = (c**2)+(b**2)
            
            # solves for the 2ab * cos(a) section of the equation.
            ab2 = (2)*(b)*(c)
            ab2 = float("-{}".format(ab2))
            ab2 = (ab2)*(math.cos(math.radians(a)))
            
            # simplifies the equation more.
            x_sq = (pythagorean_theorem)+(ab2)
            
            miss_leg = round(math.sqrt(x_sq), 2)
            
            three_legs(b,c,miss_leg,leg_3,leg_2)
    except:
        print("\n\nYour given triangle cannot exist!")
        exit()
        
try:    
    # makes the user decide if 3 legs are given or if 1 angle and 2 legs are given.
    # this is so we can make the calculations far more accurate.
    dec = input("Return 0 if 3 legs are given.\nReturn 1 if 1 angle and 2 legs are given.\n")
    
    z = False
    
    if "0" != dec:
        if "1" != dec:
            z = True
            print("\n\nYou must enter either 0 or 1!")
            exit()
            
    # asks the user to input 3 legs if they chose option 1.
    if "0" in dec:
        a = float(input("What is the first given leg?\n"))
        b = float(input("What is the second given leg?\n"))
        c = float(input("What is the third given leg?\n"))
        leg_3 = True
    else:
        # creates a boolean so we can change what to calculate in the function
        leg_3 = False
        leg_2 = True
        
    # asks the user to input 1 angle and 2 legs if they chose option 2.    
    if "1" in dec:
        a = float(input("What is the given angle?\n"))
        b = float(input("What is the first given leg?\n"))
        c = float(input("What is the second given leg?\n"))
        leg_2 = True
    else:
        # creates a boolean so we can change what to calculate in the function
        leg_2 = False
        leg_3 = True
except:
    # raises an error message for the user if they do not give a number
    if z == True:
        exit()
    print("\n\nYou must give a possible leg length for a triangle!")
    exit()

law_of_cosines_ang(a,b,c)