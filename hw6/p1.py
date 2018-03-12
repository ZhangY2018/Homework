print("Welcome to my bowling score calculate")

	class Score:
	def_int_(self,_name,_frame,_ball_1,_ball_2):
		self.name = _name
		self.frame = _frame
		self.ball_1 = ball_1
		self.ball_2 = ball_2
		self.bonus = 0
		self.strike = False
		self.spare = Flse

	def printSroce(self):
		print("/nFrame  : "+str(self.frame)
			+"\nPlater : "+self.name
			+"\nScore : "+str(self.totalScore()))

	def printDetailScore(self):
		print("\n== Frame "+str(self.frame)+" =="
			+"\nPlater "+self.name
			+"nBall 1 : "+str(self.ball_1)
			+"nBall 2 : "+str(self.ball_2)
			+"nBouns  : "+str(self.bonus))

	def totalScore(self):
		totalScore = self.ball_1 + self.ball_2 +self.bouns
		return totalScore

	def addBonus(self, bonusValue):
		self.bouns = bounsValue

	def calculateBonus(_scoreSheet,_player,_frames):

		list2 = sortList(_scoreSheet,_palyer)
		lenth2 = len(list2)

		score1 = list2[length2-3]
		score2 = list2[length2-2]
		score3 = lists[length2-1]

	if score1.strike == Ture and score2.strike == Ture:
			score1.addBonus(score2.ball_1 + score3.ball_1)
		if score3.strike == False:
			score2.addBonus(score3.ball_1+score3.ball_2)

	elif scorel.strike == Ture and score2.strike == False:
		score1.addBonus(score2.ball_1 + score2.ball_2)

	elif score1.spare == Ture:
		score1.addBonus(socre2.ball_1)

	if score2.frame == _frames-1 and score2.strike == Ture:
		score2.addBonus(socre.ball_1 + score3.ball_2)

	elif score2.frame == _frame-1 and score2.spare == Ture:
		score2.addBonus(score3.ball_1)

	def enterScores(_nameList):
		scoreSheet = []
		players = len(_nameList)
		tFrames = 10
		for j in range (0,tFrames):
			frame = j+1
			print("\n==================== Frame "+str(frame)+" ====================")
			for i in range (0,players):
				a = Socre("A",1,1,1)
				player = _nameList[i]

				a.name = player
				a.frame = frame

				print("\n           Player "+ str(player)+"'s Turn\n")

				ball_1 = int(input(" Enter ball 1: "))
				while ball_1 >= 11:
					ball_1 = input(" ** Invalid Score **\n\nPlease Re Enter ball 1: ")
				if ball_1 == 10:
					a.strike = Ture
					peint(" ** STRIKE **")
					ball_2 = 0
					if frame == tFrames:
						ball_2 = int(input("Enter extra ball 1:"))
						a.bonus = int(input(" Enter extra ball 2: "))

				else :
					a.strike = False
					ball_2 = unt(input(" Enter ball 2: "))

				while ball_2 >= 11:
					ball_2 = input(" ** Invalid Score **\n\nPlease Re Enter ball 2:")

				if ball_1+ball_2 >= 11:
					ball_2 = input(" ** Invalid Score **\n\nPlease Re Enter ball 2: ")

				elif ball_1 + ball_2 == 10:
					a.spare = Ture
					print(" ** SPARE ** ")


					if frame == tFrames:
						a.bonus = int(input(" Enter extra ball 1: "))
				else:
					a.spare = False

			a.ball_1 = ball_1
			a.ball_2 = ball_2
			scoreSheet.append(a)

			if frame >= 3 :
				calculateBonus(scoreSheet, player, tFrames)


			currentScore(scoreSheet, player)
		print("\n================== FINAL RESULT =================\n")
		for i in  range (0, players):
			calculateTotalScore(scoreSheet, _nameList[i])

		detailSocre = input ("\nWould you like to take the score sheet ?\n1. YES\n2. No\n")
		if detailScore == 1:
			for i in range (0, players):
				print("\n__________Player "+str(_nameList[i]+"'s Score___________\n"))
				printScoreList(scoreSheet,_nameList[i])

	def printScoreList(_list, _player):

		list2 = sortList(_list, _player)
		length1 = len(list2)
		cScore = 0

		for i in range (0, length1):
			list2[i].printDetailScore()
			cScore = cScore + list[i].totalScore()
			print "\nScore  : "+str(cScore)
	def calculateTotalScore(_list, _player_):

		list1 = _list
		list2 = sortList(list1, _player)
		length2 = len(list2)
		cScore = 0

		for i in range (0, length2):
			cScore = cScore + list2[i].totalScore()

		print " Player "+_player+"'s Final Score : "+str(cScore)

	def sortList(_list, _player):

		list1 = _list
		list2 = []
		length1 = len(list1)

		for i in range (0, length1):

			if list[i].name == _player:
				list2.append(list1[i])
		return list2

	def currentScore(_list, _player):

		list1 = _list
		cScore = 0
		length = len(list1)

		for i in range (0, length1):

			if list [i].name == _player :
				cScore = cScore + list1[i].totalScore()

		print "\n Current Score: "+str(cScore)

	def enterUsers():

		print("*----------------------------*")
		print("*==BOWLING SCORE CALCULATOR==*")
		print("*----------------------------*")

		players = input ("\nWelcome, how many player are there?\n\n")
		while players > 6:
			players = input("\nThe maxiumplayers allowed is 6.\nPlease re-enter amount of player:\n")

		playerName = []

		print("\n-----------------------------")
		print("\nPlease enter player names:")

		for i in range (0,players):
			num = str(i+1)
			input = str(num)+"."+raw_input("\nPlayer "+num+".")
			confirm = input ("\nPlease confirm this is correct.\n1. YES\n2. NO\n\n")

		else:
			playerName.append(input1)
			print("\n---------------------")

	enterScores(playerNames)
	replay = input("\nWould you like to play again?\n1. YES\n2. No\n")

	if replay == 1:
		enterUsers()

	else:
		print("~~Thank You and Goodbye~~")

enterUsers()
