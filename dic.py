# using dictionary

d= dict() # define a new empty dictionary
number = int(input("Enter integer: "))

for i in range(1,number+1):
	d[i] = i*i
	
print d
