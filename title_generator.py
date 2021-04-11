p1 = input("Please input a sentence.\n")
p1 = p1.lower()

def title_creator(p1):
    p = p1.split()
    p_len = len(p)
    
    d = []
    
    for i in range(p_len):
        p[i] = p[i][0].upper() + p[i][1:]
        
        if p[i] == "And":
            p[i] = p[i][0].lower() + p[i][1:]
        if p[i] == "Or":
            p[i] = p[i][0].lower() + p[i][1:]
        if p[i] == "But":
            p[i] = p[i][0].lower() + p[i][1:]        
        
    p = " ".join(p)        
    
    return p
    
z = title_creator(p1)
print(z)