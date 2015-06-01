from random import random

def nNumGen(n):
	"""
	return an "n" digit string of numerals
	"""											
	return str(random())[2:n+2]
	
def checker(x, y):
	"""
	checks for values which are the same in the same position and different positions in strings x and y.
	
	keyword arguments:
	x -- the string being checked
	y -- the string being checked against
	
	returns:
	in_pos -- the number of indexes with same values in both x and y
	x_in_z -- the number of values in x which are also in y, but have a different index to each different value
	"""
	x = list(x)
	z = list(y)								#creates a copy, which is mutable, of y
	in_pos, x_in_z = (0, 0)					#each variable is a counter, which will be used for the returns
	for i in range(len(x)):					
		if x[i] == z[i]:
			in_pos += 1						
			z[i] = 'p'						#p is a place holder. means x_in_z does not get confused by values
			x[i] = 'k'
	for i in range(len(x)):
		if x[i] in z:						#which it has already counted
			x_in_z += 1						#this is important, otherwise two numbers in x could reference a single
			z[z.index(x[i])] = 'p'			#number in z, whilst only one of them is correct, but in the wrong position
	return (in_pos, x_in_z)
	'''
	should check for in_pos first! before x_in_z, otherwise, x_in_z check will delete numbers which might be in position :((((
	'''
	'''
	should only check x_in_z for values which have not already been proved +ive in in_pos :('''

def masterMind(g):
	"""
	play a full game of mastermind. user chooses "n", the number of digits of the numbe they must guess. The function
	gives feedback after each turn, based upon how many of the digits the player guessed are correct and in the right
	place, or just correct, but in the wrong place
	
	keyword arguments:
	g -- the number of turns in which a player has to guess the guess the secret number
	"""

	k = raw_input("How many digits would you like to guess?\n==> ")
	while True:													#Until loop is broken, it willcontinue to ask for a 
		try:													#guess. Will only break loop, and continue game, if	
			k = int(k)											#an integer is entered. fairly robust
			break
		except:
			print "Please enter a valid number"
			
	print "You have " + str(g) + " guesses! \n"

	code = nNumGen(k)																#sets the secret number/answer
	
	for r in range(g):																#for each "game turn"/play a round
		while True:																	#as above, will continue to ask for
			guess = raw_input("what is your guess? ")								#user input till a correct input is
			try:																	#entered.
				if len(guess) != len(code):											#loop continues if guess is the same
					raise exception													#length as the code, and an integer
				int(guess)
				break
			except:
				print "Invalid input"
		if guess == code:						#checks for a win, gives feedback and returns the function if there is one
			print "Congratulations, you won in", r + 1, "turns, with", g - r - 1, "turns to spare."
			return
		a, b = checker(guess, code)				#gives feedback on the guess if there isn't a winning guess
		print "Your guess has", a, "digits in the correct position and", b, "out of position"
	print "You have run out of guesses!\nThe secret number was " + code            #in case of loss
	
masterMind(11)