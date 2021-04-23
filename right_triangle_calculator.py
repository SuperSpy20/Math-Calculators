import math
try:
    p = float(input("What is the angle you are measuring (in degrees)?\n"))
    c_given = input("Is the given leg the hypotenuse, opposite, or adjacent?\n").lower()
    c_1 = float(input("What is the length of the given leg?\n"))

    if p < 0.0:
        p = abs(p)
    
    if p >= 90.0:
        p_1 = True
        print("\n\nThe angle you are measuring must be acute!")
        exit()
    else:
        p_1 = False
    
    if "hyp" in c_given:
        x = True
    else:
        x = False
                
    if "opp" in c_given:
        y = True
    else:
        y = False

    if "adj" in c_given:
        z = True
    else:
        z = False
except:
    if p_1 == True:
        exit()
    print("\n\nYou must give an angle less than 90 degrees and give a specific leg length!")
    exit()
    
opp_angle = (90)-(p)

def angle_leg_algebra(p, c_1):
    if x == True:
        hyp = c_1
        
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        opp = (s)*(c_1)
        opp = round(opp, 2)
        
        g = math.cos(math.radians(p))
        g = round(g, 2)
        
        adj = (g)*(c_1)
        adj = round(adj, 2)
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
    if y == True:
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        hyp = (c_1)/(s)
        hyp = round(hyp, 2)
        
        opp = c_1
        
        t = math.tan(math.radians(p))
        t = round(t, 2)
        
        adj = (c_1)/(t)
        adj = round(adj, 2)
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
    if z == True:
        c = math.cos(math.radians(p))
        c = round(c, 2)
        
        adj = c_1
        
        hyp = (c_1)/(c)
        hyp = round(hyp, 2)
        
        s = math.sin(math.radians(p))
        s = round(s, 2)
        
        opp = (s)*(c_1)
        opp = round(opp, 2)        
        
        v = "Opposite Leg: {}\nHypotenuse: {}\nAdjecent Leg: {}\nOpposite Angle: {}".format(opp, hyp, adj, opp_angle)
        return v
        
j = angle_leg_algebra(p, c_1)

print("\n{}".format(j))
