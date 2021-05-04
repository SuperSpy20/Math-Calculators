import statistics
import math

def standard_deviation(set):
    def sample(set_samp):
        q = sum(set_samp)
        p = len(set_samp)
        p = (p)-(1)

        f = (q)/(p)
        return f
    
    print("\nYour given set: {}".format(set))

    avg_1 = statistics.mean(set)


    for z, i in enumerate(set):
        set[z] = (i)-(avg_1)

    for z, i in enumerate(set):
        set[z] = math.pow(set[z], 2)


    set_samp = sample(set)

    avg_2 = statistics.mean(set)

    avg_2_sqrt = math.sqrt(avg_2)
    avg_sqrt = math.sqrt(set_samp)

    print("\nPopulation Standard Deviation: {}".format(round(avg_2_sqrt, 2)))
    print("Sample Standard Deviation: {}".format(round(avg_sqrt, 2)))

set = input("What is your given set/list?\n").split(",")
standard_deviation(set)
