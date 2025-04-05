
import random 

magic8answers = ['It is certain',  'It is decidedly so',  'Yes',  'Reply hazy try again',  
				 'Ask again later',  'Concentrate and ask again',  'My reply is no',  
				 'Outlook not so good',  'Very doubtful']

answerStats = [0,0,0,0,0,0,0,0]		
statsTotal = 0		 

def updateStats(idx):
	# Update the statistics array and total variable
	# Demo the need for global when updating a variable that isn't an array 
	
	global statsTotal 
	answerStats[idx] += 1

	statsTotal = 0
	for x in range(8):
		statsTotal += answerStats[x]


def getAnswer(): 
	# Retrieve a random answer from the magic 8 ball 

	answerIdx = random.randint(0,7)
	updateStats(answerIdx)
			
	return magic8answers[answerIdx]


# call the 8 ball multiple times to load the stats array with some random data
for x in range(42):
	getAnswer()

print(getAnswer())

print(answerStats, statsTotal)
