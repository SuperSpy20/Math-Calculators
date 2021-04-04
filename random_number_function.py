import random
import numpy

try:
    random_input = input('Please input a range. (from 0 to whatever number you choose)\n')
    p = int(random_input)

    if p == 0:
        print('\n\nThe range must not be zero!')
        exit()


    def random_number(last_number):
        last_number = (last_number) + 1
        
        d = []
        
        for x in range(last_number):
            d.append(x)

        d = random.choice(d)
        
        d = "{:,}".format(d)

        return d

    b = random_number(p)

except:
    print('\n\nYou must enter a valid integer!')
    exit()

print('\nYour Random Number is: %s'%b)

