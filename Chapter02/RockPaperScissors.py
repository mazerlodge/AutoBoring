
import random

print("Rock, Paper, Scissors")

winCount = 0
tieCount = 0
loseCount = 0 
playerChoice = 'NOT_SET'

def spellOutChoice(letterChoice): 
	# return spelled out version of letterChoice (e.g. given 'r', return 'Rock')
	rval = "?" 

	if (letterChoice == 'r'): 
		rval = 'Rock'
	elif (letterChoice == 'p'):
		rval = 'Paper' 
	elif (letterChoice == 's'): 
		rval = 'Scissors'

	return rval  

def getComputerChoice(): 
	# returns one of r, p, s
	hands = ['r', 'p', 's']
	idx= random.randint(0,2)

	return hands[idx]


def getPlayerChoice():
	# return one of r, p, s, q 
	rval = "NOT_SET"

	while rval == "NOT_SET":
		print("Enter your choice; (r)ock (p)aper (s)cissors or (q)uit")
		playerChoice = input() 

		if (playerChoice.lower() == 'r' 
	  		or playerChoice.lower() == 'p'
			or playerChoice.lower() == 's'
			or playerChoice.lower() == 'q'):
			rval = playerChoice.lower()

	return rval

def evaluateChoices(playerChoice, computerChoice):

	print('Player chose %s, Computer chose %s' % (spellOutChoice(playerChoice), 
											  spellOutChoice(computerChoice)))
	
	# Convert player and computer choices to numbers (r,p,s becomes 0,1,2)

	# TODO: Do eval
	evalGrid = [
					[2, 1, 0],
					[0, 2, 1],
					[1, 0, 2]
				]
	


	# TODO: Update stats 

	print('%d Wins, %d Losses, %d Ties' % (winCount, tieCount, loseCount))

while (playerChoice != 'q'):
	computerChoice = getComputerChoice()
	playerChoice = getPlayerChoice()

	if (playerChoice != 'q'):
		evaluateChoices(playerChoice, computerChoice) 




	





