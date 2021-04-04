try:
    average_input = input('What are the numbers you want to find of the average of?\n').split(',')

    p = list(map(int, average_input))
except:
    print('\n\nYou must enter a proper list!')
    exit()
    
def average(list_1):
    b = sum(list_1)
    a = len(list_1)

    z = (b)/(a)

    return z

average_calculation = average(p)

print('\nAverage: %s'%average_calculation)