#!/bin/python 

# Demo a random number of range 1 to n can be obtained via n * (rnd(100)/100)

valList = []
for x in range(1,32):
	valList.append(0)

for i in range(1,101):
	cv = int(30 * (i/100))
	valList[cv] = valList[cv] + 1
	
# calc total hits 
totalHits = 0
for x in valList:
	totalHits = totalHits + x  

# output distribution
pctTotal = 0
for x in range(0,len(valList)): 
	if (valList[x] > 0): 
		pct = valList[x]/totalHits
		pctTotal = pctTotal + pct 
		print(x, " = ", valList[x], " ", pct)
	else:
		print(x, " NO Vals")
print("% Total = ", pctTotal)