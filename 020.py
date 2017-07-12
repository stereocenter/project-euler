import math

x = 100
fact = str(math.factorial(x))
length = len(fact)
index = length - 1

#print(x)
#print(fact)
#print(length)
#print(fact[index])

sum = 0
while index >= 0:
	sum = sum + int(fact[index])
	index -= 1
	
print(sum)
