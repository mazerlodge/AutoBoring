
def collatz(num): 
	rval = 0

	if (num % 2 == 0): 
		rval = num // 2
	else: 
		rval = 3 * num + 1

	print(rval) 

	return rval 

# main loop 
numToCheck = -1 

while (numToCheck == -1):
	try: 
		numToCheck = int(input("Enter a positive number (0 to quit):"))

		if numToCheck < 0:
			numToCheck = -1

	except ValueError: 
		print("The program requires an integer to continue.")
		numToCheck = -1

print(numToCheck)
while (numToCheck > 1):
	numToCheck = collatz(numToCheck) 
