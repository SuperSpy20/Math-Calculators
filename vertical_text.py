p = input("What is your vertical text?\n")

d = []
for i in p:
    d.append(i)

for z, i in enumerate(d):
    d[z] = "\n{}".format(i)

d = "".join(d)
	
print(d)