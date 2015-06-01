from shuffle import shuffle							#makes the function shuffle available

def deck_gen(N = 52):									#might replace/rename this
	deck = range(N)
	for n in deck:
		deck[n] %=13
		deck[n] += 1
	return deck

def add_to_11(visible):
	"""
	return a tuple of the indices of the cards which add to 
	eleven, or if no cards satisfy this condition, return and empty tuple
	
	works by checking the addition of each pair of any two 
	numbers in the list visible for a value of eleven.
	
	keyword arguemnts:
	visible -- the list of faceup cards on the piles on the table
	"""
	lenvis = len(visible)
	for i in range(lenvis):							#for each item in visible, adds it to all following items. If the two numbers sum to eleven, their indexes are returned.
		for n in range(i+1, lenvis):
			if visible[i] + visible[n] == 11:
				return (i, n)
	return ()										#iff no sums to eleven are found, the function will return an empty tuple

def jqk(visible):												
	"""
	return a tuple of the indices of the cards which form a
	set of jack quen and king, or if no cards satisfy this condition,
	return and empty tuple
	
	keyword arguemnts:
	visible -- the list of faceup cards on the piles on the table
	"""
	jqk = [0, 0, 0]									
	if 11 in visible and 12 in visible and 13 in visible:		#function checks for 11s, 12s and 13s. If each is there, it makes the index, of the first instance of each, the elements of the list jqk. Else it returns an empty tuple
		return (visible.index(11), visible.index(12), visible.index(13))
	else:
		return ()

def play(deck, verbose):
	"""
	play a single game of patience with a deck. Return the number
	of cards left in the deck at the end of the game, and therefore
	if 0 is returned, the game has been won. If verbose, prints the
	visible cards at each stage of the game.
	
	keyword arguments:
	deck -- a list representing a deck.
	verbose -- Boolean value controlling whether the visible cards are
	printed at each stage of the game.
	"""
	shuffle(deck)
	visible = [deck.pop(0), deck.pop(0)]									#creates list "visible" which contains the face up cards, and makes the top two cards of the deck the first two elements.
	if verbose:																
		print visible
		
	while len(deck) > 0 and len(visible) < 10:								#while game winning conditions (the length of deck becoming 0, or more than 9 piles being created) are not met, play the game.
		if add_to_11(visible) != ():										#if add_to_11(visible) does not equal (), it means there are cards to be replaced
			a, b = add_to_11(visible)										#unpack the indices of two cards which add to eleven
			visible[a] = deck.pop(0)
			if len(deck) > 0:												#for the case where the length of the deck is 1 at the start of the loop, this ensures the computer doesn't try to access an element in a empty list.
				visible[b] = deck.pop(0)
		elif 11 in visible and 12 in visible and 13 in visible:				#checks for j, q, k in visible
			a, b, c = jqk(visible)											#unpacks the indices of j, q and k.
			visible[a] = deck.pop(0)
			if len(deck) > 1:
				visible[b] = deck.pop(0)
			if len(deck) > 1:
				visible[c] = deck.pop(0)
		else:																#if the above two conditions have not been met, a new pile must be created
			visible.append(deck.pop(0))
		if verbose:
			print visible
			
	if len(visible) == 10:													#if a tenth pile has to be turned over, the game is lost, so the card in the tenth pile is returned to the deck.
		deck.append(visible.pop(9))
	return len(deck)														#returns the length of the deck as described in the docstring

def many_plays(N):
	"""
	return a list 'remaining' in which the value of the elements
	represent the number of times a game ends with a number of cards
	left in the deck equal to the index of that element. ie.
	remaining[6] would be the number of times a game ended with
	six cards left in the deck
	
	keyword arguments:
	N -- the number of games to be played.
	"""
	remaining = 53*[0]														#empty list where the index represents the number of cards remaining at the end of a game of a patience, and the value at each index is the number of of games of patience that returned that result
	for n in range(N):
		remaining[play(deck_gen(), False)] += 1
	return remaining
	
from histogram import histogram

if __name__ == "__main__":
	deck_of_cards = deck_gen()
	print play(deck_of_cards, True)
	histogram(range(53), many_plays(10000), 55)