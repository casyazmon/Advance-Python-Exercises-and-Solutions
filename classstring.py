# a class that get a string from the keyboard and print the string in upper case

class InputString:
	def __init__(self):
		self.s = ""
	
	def getString(self):
		self.s = raw_input("Enter string\n")
		
	def printString(self):
		print self.s.upper()
		
#testing our InputString class

strObj = InputString()
strObj.getString()
strObj.printString()
