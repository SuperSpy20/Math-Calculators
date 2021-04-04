import math

c_1 = input('What is the coordinate of the first point?\n')
c_2 = input('What is the coordinate of the second point?\n')

c_1 = c_1.split(',')
c_2 = c_2.split(',')

p = map(float, c_1)
q = map(float, c_2)

coordinate_distance = math.dist(p, q)

if p == q:
    print('The two points equal each other. The distance is 0.')
    exit()

print('\nDistance: %s'%coordinate_distance)