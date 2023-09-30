#!/usr/bin/python3
"""
	Demo variable scope w/ global var modified in a function
"""
def spam():
	eggs = "spam local" 
	print(eggs) 
	
def bacon(): 
	global eggs 
	eggs = "bacon local overwrite" 
	print(eggs) 
	spam() 
	print(eggs) 
	
# global scope 
eggs = "global" 
bacon() 
print(eggs) 
