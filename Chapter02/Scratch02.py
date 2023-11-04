#!/bin/python

nameList = ["Alice", "sAlice"]
ageList = [3, 12, 23]

def checkAlice(name, age):
	if name == "Alice":
		print(f"Hi, Alice. (using {name},{age})")
	elif age < 12:
		print(f"You are not Alice, kiddo. (using {name},{age})")

for n in nameList:
	for a in ageList: 
		checkAlice(n, a)	

# break example
x = 0 
while (x<7): 
	print(x) 
	x = x + 1 
	
	if (x > 5):
		break
		
# continue example
print ("Continue example")
for x in range(1,20):
	if (x % 2 == 1):
		# is odd, skip to next for value
		continue
	print(x)
		

# floating false example
v = 0.0 

if (v):
	print("0.0 was considered true.")
else:
	print("0.0 was considered false.")

# how small of an int is considered true 
d = 10.0 / 100
print(d)

print("Start small number test")
denom = 10
for x in range (1,20):
	denom = denom * 10
	smallNum = 10.0 / denom
	if (smallNum):
		print(f"{smallNum} was considered true.")
	else:
		print(f"{smallNum} was considered false.")

