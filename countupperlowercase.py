# this program count the number of upper and lower case letters in a sentence

sent = raw_input()

d = {"UPPER CASE":0,"LOWER CASE":0}
for c in sent:
	if c.isupper():
		d["UPPER CASE"]+=1
	elif c.islower():
		d["LOWER CASE"] +=1
	else:
		pass
		
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]
