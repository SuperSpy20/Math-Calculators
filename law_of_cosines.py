import math

ang = float(145)
a = float(16)
b = float(18)

def law_of_cosines(ang, a, b):

    if str(a).endswith(".0"):
        a = int(a)

    if str(b).endswith(".0"):
        b = int(b)

    if str(ang).endswith(".0"):
        ang = int(ang)        

    cos = math.cos(math.radians(ang))
    ab = (2 * a * b)
    
    a_2 = math.pow(a, 2)
    b_2 = math.pow(b, 2)
    
    pythag = (a_2) + (b_2)
    hyp_2 = (pythag) - (ab) * (cos)
    
    equation = "\nHypotenuse^2 = ({}^2 + {}^2) - (2 * {} * {}) * cos({})".format(a, b, a, b, ang)
    print(equation)
    
    hyp = math.sqrt(hyp_2)
    hyp = round(hyp, 2)
    
    hyp_2 = round(hyp_2, 2)
    print("\nHypotenuse Squared: {}".format(hyp_2))
    
    return hyp
    
print("Hypotenuse: {}".format(law_of_cosines(ang, a, b)))