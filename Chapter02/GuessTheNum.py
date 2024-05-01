#!/bin/python 

# Ref: https://automatetheboringstuff.com/2e/chapter2/
# Section Heading 'A Short Program: Guess the Number'

import random

LOW_NUM = 1 
HIGH_NUM = 20
secretNum = random.randint(LOW_NUM, HIGH_NUM)
print(f"I am thinking of a number between {LOW_NUM} and {HIGH_NUM}")

# Ask the player to guess 6 times 
for guessTaken in range(1,7): 
	playerNum = int(input("Take a guess: ")) 
	if (playerNum < secretNum): 
		print('Your guess was too low')
	elif (playerNum > secretNum): 
		print('Your guess was too high')
	else: 
		break;

if playerNum == secretNum:
	print(f'Good job! You guessed my number in {guessTaken}')
else: 
	print(f'The number I was looking for was {secretNum}')



		
