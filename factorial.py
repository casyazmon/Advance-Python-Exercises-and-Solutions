# python program to compute the factorial of a number

#factorial = 1
#print "Enter a positive integer"
#num = int(raw_input())

#if num < 0:
#	print(" Factorial does no exist for negative numbers\n")
#elif num == 0:
#	print "0! = 1"
#else:	
#	for i in range(1,num+1):
#		factorial = factorial*i
		
#print num,'!= ', factorial 
	
	
def fac(num):
	if num == 0:
		return 1
	else:
		return num*fac(num-1)
		
num1 = int(input("Enter number: "))
print num1,"! = ", fac(num1)
