#!/usr/bin/python3
"""
	Demo variable scope
"""
def spam():
	eggs = "spam local" 
	print(eggs) 
	
def bacon(): 
	eggs = "bacon local" 
	print(eggs) 
	spam() 
	print(eggs) 
	
# global scope 
eggs = "global" 
bacon() 
print(eggs) 
