import math

decision = "0"#input("Return 0 if two angles and one leg are given. Return 1 if one angle and two legs are given.\n")

if "0" in decision:
    ang_2 = True
else:
    ang_2 = False

if "1" in decision: 
    leg_2 = True
else:
    leg_2 = False
    
def law_of_sines():    

    if ang_2 == True:
        # gather input
        angle_1 = float(input("What is the first angle (in degrees)?\n"))
        angle_2 = float(input("What is the second angle?\n"))
        leg = float(input("What is the given leg length?\n"))
        angle_3 = (180) - (angle_1) - (angle_2) 
 
        # gather sines
        sin_2 = math.sin(math.radians(angle_1))
        sin_1 = math.sin(math.radians(angle_2))
        sin_3 = math.sin(math.radians(angle_3))
        
        # do calculations
        ratio = (leg) * (sin_2)
        leg_2 = (ratio) / (sin_1)
        
        ratio = (leg) * (sin_3)
        leg_3 = (ratio) / (sin_1)

        # round calculations
        angle_1 = round(angle_1, 2)
        angle_2 = round(angle_2, 2)
        angle_3 = round(angle_3, 2)
        leg = round(leg, 2)
        leg_2 = round(leg_2, 2)
        leg_3 = round(leg_3, 2)
            
        # make .0's whole numbers.    
        whole = [angle_1, angle_2, angle_3, leg, leg_2, leg_3]
        
        for i, z in enumerate(whole):
            if str(whole[i]).endswith(".0"):
                whole[i] = int(whole[i])
                
        angle_1 = whole[0]
        angle_2 = whole[1]
        angle_3 = whole[2]
        leg = whole[3]
        leg_2 = whole[4]
        leg_3 = whole[5]

        

        v = "Leg A = {}\nLeg B = {}\nLeg C = {}\n\nAngle A = {}°\nAngle B = {}°\nAngle C = {}°".format(leg, leg_2, leg_3, angle_1, angle_2, angle_3)
        return v
        
    if leg_2 == True:
        angle = input("What is the given angle (in degrees)?\n")
        leg_1 = input("What is the first leg length?\n")
        leg_2 = input("What is the second leg length?\n")
        
        

print("\n{}".format(law_of_sines()))