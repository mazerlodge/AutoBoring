#!/bin/python 

# Basic command line IO example.

print('Hello World!') 

print('What is your name?')
myName = input()

print('It is good to meet you, ' + myName)

print('The length of your name is:')
print(len(myName))

print('What is your age?')
myAge = input() 
print('You will be ' + str(int(myAge) + 1 ) + ' in a year.')

print('Enter pi so I can do math on a floating point number:')
piVal = input() 

newFloat = float(piVal) * 1.42
print('New float is ' + str(newFloat))

# an uncommon math operator, integer divison/floored quotient 
idfq = 22 // 8
print('22 div 8 with quotient floored = ' + str(idfq)) 

# Using splat on strings 
dupy = 'Alice ' * 5
print(dupy)
