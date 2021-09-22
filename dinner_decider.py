import random

def main():
    b = True

    p = input("What resturaunts are you considering?\n")

    p_lower = p.lower()

    d = p.split(",")
        
    # error handling
    def dont_know_msg():
        x = input("\n\nWhat do you mean you don't know?\nTry again? (y/n)")
        if x.startswith("y"):
            main()
        if x.startswith("n"):
            exit()

    # checking if the user didn't know, and executed the 'dont_know_msg' function
    if "don't know" in p_lower:
        dont_know_msg()
        b = False
        
    if "dont know" in p_lower:
        dont_know_msg()
        b = False
        
    # this boolean is used to check if the code passed the checks, so it doesn't do it twice.
    if b == True:
        print("\nI choose: {}".format(random.choice(d)))
    
main()