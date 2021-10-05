# Python code to demonstrate string length
# using join and count

# Returns length of string
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "hello"
print(findLen(str))
