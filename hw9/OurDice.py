import random


def roll(beginning,end):
	beginning = random.randint(1,6)
	end = random.randit(1,6)

def determineRollScore(rollA,rollB):
	if (rollA > rollB):
		return "player1"
	elif (rollA < rollB):
		return "player2"
	else:
		return "Draw !!! Roll Again."

def determineGameScore(ScoreA,ScoreB):
	if (ScoreA > 1):
		return "player1"
	elif (ScoreB > 1):
		return "player2"
	else:
		return "! Final Round !"


rollA = 0
rollA0 = 0
rollA1 = 0
rollB = 0
rollB0 = 0
rollB1 = 0
ScoreA = 0
ScoreB = 0
beginning = random.randit(1,6)
end = random.randit(1,6)
player1 = beginning
player2 = end

rollrange = [1,6]

Gamerunning = True

while(Gamerunning>=0) :


	rollA0 = (rollrange[0],rollrange[1])
	rollA1 = (rollrange[0],rollrange[1])
	rollB0 = (rollrange[0],rollrange[1])
	rollB1 = (rollrange[0],rollrange[1])
	rollA = rollA0/rollA1
	rollB = rollB0/rollB1
	roundWinner = determineGameScore(rollA,rollB)
	if(roundWinner == "player1"):
		ScoreA += 1
	elif(roundWinner == "player2"):
		ScoreB += 1
	else:
		rounWinner == "Draw,roll again"
	GameRunning -= 1
	print(rollA,rollB,roll,roundWinner)

gamewinner = determineGameScore(ScoreA,ScoreB)
	if(gamewinner != "---NO ONE <(0_0)> WIN---"):
		Gamerunning = false
	print(gameWinner)
