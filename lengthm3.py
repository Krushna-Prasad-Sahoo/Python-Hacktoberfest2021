# Python code to demonstrate string length
# using while loop.

# Returns length of string
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "Hello"
print(findLen(str))
