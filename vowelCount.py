# this program count the number of vowels in a sentence

s = raw_input()
vowelcount=0
vowels = ('a','e','i','o','u')
for i in s:
	if i in vowels:
		vowelcount +=1
print vowelcount

