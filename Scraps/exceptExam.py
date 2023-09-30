#!/usr/bin/python3 
"""
Exception handling example 
"""
def spam(divBy): 
	try: 
		return 42 / divBy 
	except ZeroDivisionError: 
		print('Error: Invalid Argument [%d]' % divBy) 

		
# main entry point
testVals = [2, 12, 0, 1]
for aVal in testVals: 
	print(spam(aVal)) 

