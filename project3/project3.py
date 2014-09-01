################################################
#
#  Project 3    March 21, 2014
#  Game of Sticks, with AI
#
#  Matthew Leeds
#
#  File: project3.py
#
################################################

import random

def main():
	option = ''
	while True:
		print()
		print("Welcome to the game of sticks!")
		print()
		print("(1) Play against a friend")
		print("(2) Play against an unskilled AI")
		print("(3) Play against a skilled AI")
		print("(4) Exit")
		print()
		option = input("   Enter an option...")
		if option == '4': break
		elif option in ['1','2','3']:
			initialSticks = ''
			print()
			initialSticks = int(input("How many sticks are initially on the table (10-100)? "))
			if initialSticks < 10 or initialSticks > 100: 
				print("Please enter a valid number of sticks between 10 and 100, inclusive.")
				continue
			elif option == '1': vsHuman(initialSticks)
			elif option == '2': vsUnskilledAI(initialSticks)
			elif option == '3': vsSkilledAI(initialSticks)
		else: print("Invalid option. Please enter a number 1-4.")

def vsHuman(currentSticks): # this function only supports 1 round, but you can come back to it
	currentPlayer = '1' # player 1 always starts first
	while True:
		print()
		print("There are " + str(currentSticks) + " sticks on the board.")
		takeSticks = int(input("Player " + currentPlayer + ": How many sticks do you take (1-3)? "))
		if takeSticks not in [1,2,3]:
			print("Please enter a valid number of sticks to take (1, 2, or 3).")
			continue 
		elif takeSticks > currentSticks: takeSticks = currentSticks # they can't take more than exist
		if currentSticks == takeSticks: 
			print()
			input("Player " + currentPlayer + ", you lost the game.")
			return
		else: # only possibility left is takeSticks < currentSticks
			currentSticks -= takeSticks # update stick count
			if currentPlayer == '1': currentPlayer = '2' # switch to the other player's turn
			else: currentPlayer = '1'

class Hat(object):
	def __init__(self):
		self.content = [1,2,3]
		self.beside = []
		self.beside2 = []
	
	def getRandom(self): 
		# this returns a random number from content, and adds it to beside
		randomIndex = random.randint(0,len(self.content)-1)
		pick = self.content[randomIndex]
		self.content.remove(pick)
		return pick

	def __str__(self):
		# a printable version for debugging purposes
		return "[ content: " + str(self.content) + " beside: " + str(self.beside) +\
		" beside2: " + str(self.beside2) + " ]"

def vsUnskilledAI(initialSticks, ListOfHats=None):
	currentSticks = initialSticks

	# The AI should set up its hats before the game starts
	if not ListOfHats: 
		ListOfHats = []
		for i in range(currentSticks):
			ListOfHats.append(Hat())
	
	while True: # this is the loop for each round of the game
		print()
		print("There are " + str(currentSticks) + " sticks on the board.")
		
		# Player 1's turn
		takeSticks = int(input("Player 1: How many sticks do you take (1-3)? "))
		if takeSticks not in [1,2,3]:
			input("Please enter a valid number of sticks to take (1, 2, or 3).")
			continue
		elif takeSticks > currentSticks: takeSticks = currentSticks # they can't take more than exist
		if currentSticks == takeSticks:
			again = input("Player 1, you lost the game. Play again? (y/n) ")
			if again == 'y' or again == 'Y': 
				currentSticks = initialSticks # reset the game
				continue
			else: return # exit to main
		else: # only possibility left is takeSticks < currentSticks
			currentSticks = currentSticks - takeSticks
		
		print()
		print("There are " + str(currentSticks) + " sticks on the board.")

		# AI's turn
		takeSticks = (ListOfHats[currentSticks-1]).getRandom() 
		# this should pick a random number from the appropriate hat
		
		(ListOfHats[currentSticks-1]).beside.append(takeSticks)
		# this adds the pick to beside. Somehow this wasn't in the version I turned in.

		print("AI selects " + str(takeSticks))
		if takeSticks >= currentSticks: # The AI lost.
			again = input("The AI lost the game. Play again? (y/n) ")
			if again == 'y' or again == 'Y': 
				currentSticks = initialSticks # reset the game
				continue
			else: return # exit to main
			# We throw away all the items we picked unless 
			# they are the only instance of that number for that hat
			for item in ListOfHats:
				if len(item.beside) != 0:
					if item.beside[0] not in item.content: # it's the last instance of that number
						item.content = item.content + item.beside # add it to the main list
					item.beside = [] # empty all the besides
		else: currentSticks = currentSticks - takeSticks
		if currentSticks == 1: # The AI won!
			# Look for all the ones we picked and add them to content twice
			for item in ListOfHats:
				if len(item.beside) != 0:
					item.content.append(item.beside[0])
					item.content.append(item.beside[0])

def vsSkilledAI(initialSticks):
	numRounds = 100000 # number of games the AI's will play
	# The AI's will use the same list of hats but separate besides
	ListOfHats = []
	for i in range(initialSticks):
		ListOfHats.append(Hat())
	
	# Now the AI's will play each other for numRounds rounds
	print()
	print("Training the AI...")
	print()
	for i in range(numRounds): 
		currentSticks = initialSticks
		turnCounter = 0
		while True:
			turnCounter += 1
            # odd numbers = AI-1, even numbers = AI-2
			takeSticks = (ListOfHats[currentSticks-1]).getRandom()
			
			# if turnCounter % 2 == 1: print("AI-1 chose " + str(takeSticks) + " of " + str(currentSticks))
			# else: print("AI-2 chose " + str(takeSticks) + " of " + str(currentSticks))

			# Add the picked number to the appropriate beside.
			if turnCounter % 2 == 1: # AI-1
				(ListOfHats[currentSticks-1]).beside.append(takeSticks)
			else: # AI-2
				(ListOfHats[currentSticks-1]).beside2.append(takeSticks)

			if takeSticks >= currentSticks: # game over
				for item in ListOfHats:
					if turnCounter % 2 == 1: # AI-1 lost
						if len(item.beside) != 0: # only look at besides that aren't empty
							if item.beside[0] not in item.content: # make sure it's not the last instance of a #
								item.content += item.beside
							item.beside = []
						if len(item.beside2) != 0: # double up the ones that worked for AI-2
							item.content.append(item.beside2[0])
							item.content.append(item.beside2[0])
							item.beside2 = [] # clear out the besides before next round

					else: # AI-2 lost
						if len(item.beside2) != 0: # clear out the besides unless they're the last instance of a #
							if item.beside2[0] not in item.content: 
								item.content += item.beside2
							item.beside2 = []
						if len(item.beside) != 0: # double up the ones that worked for AI-1
							item.content.append(item.beside[0])
							item.content.append(item.beside[0])
							item.beside = [] # clear out the besides before next round
	
				break # next round
			else: # takeSticks < currentSticks; the game continues 
				currentSticks -= takeSticks
		
	vsUnskilledAI(initialSticks,ListOfHats)	# use the code for the unskilled version, 
	# but pass it the list of hats from after the training, and the # of sticks the user chose

main()
