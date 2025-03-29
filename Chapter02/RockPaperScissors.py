
import random

print("Rock, Paper, Scissors")

outcomeCounts = [0,0,0]
WIN_IDX = 0
LOSE_IDX = 1
TIE_IDX = 2 
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
	hands = ['r', 'p', 's']
	playerChoiceIdx = hands.index(playerChoice)
	computerChoiceIdx = hands.index(computerChoice) 
	
	# Do evaluation
	evalGrid = [
					[2, 1, 0],
					[0, 2, 1],
					[1, 0, 2]
				]
	outcomes = ['Player wins', 'Computer Wins', 'Tie']
	outcomeIdx = evalGrid[playerChoiceIdx][computerChoiceIdx]

	print('Indexes for player=%d and computer=%d outcome=%d' % 
		    (playerChoiceIdx, computerChoiceIdx, outcomeIdx))

	# Update stats and display them 
	outcomeCounts[outcomeIdx] += 1
	print('%d Wins, %d Losses, %d Ties' % 
		   (outcomeCounts[WIN_IDX], outcomeCounts[LOSE_IDX], outcomeCounts[TIE_IDX]))

# Main loop starts here 
while (playerChoice != 'q'):
	computerChoice = getComputerChoice()
	playerChoice = getPlayerChoice()

	if (playerChoice != 'q'):
		evaluateChoices(playerChoice, computerChoice) 

