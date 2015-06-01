import random

def shuffle(a_list):
	"""
	shuffle the list a_list in place
	
	keyword arguments:
	a_list -- the list to be shuffled.
	"""
	if type(a_list) != list:
		return "invalid argument"
	N = len(a_list)									#N = number of elements
	for i in range(N-1, 0, -1):						#for i from N-1 downto 1 do:
		j = int(random.random()*(i+1))				#j = random integer such that 0 <= j <= i
		a_list[i], a_list[j] = a_list[j], a_list[i]					#swap a_list[i] and a_list[j]
	
	return a_list

def check_shuffle(a_list):
	"""
	check two conditions:
	1. That the shuffled list and original list are the same length
	2. i) That every element from the original and ii) only the
	elements from the original are in the shuffled 
	
	keyword arguments:
	a_list -- the list, the shuffling of which is to be checked
	"""
	if type(a_list) != list:
		return "invalid argument"
	source = a_list									#source is the original list
	shuffle(a_list)									#shuffles a_list, so now a_list has the shuffled values
	if len(a_list) != len(source):					#checks condition 1. the lengths.
		return False
	for i in range(len(source)):			
		if source[i] not in a_list:					#checks condition 2. i
			return False
		if a_list[i] not in source:					#checks condition 2. ii)
			return False
	return True

def quality(a_list):									#defensive code here to check that the a_list is a list of unique numbers?
	"""
	check the quality of a function "shuffle" of a list "a_list"
	by finding the ratio of consecutive pairs in which the latter
	is the greater to the pairs in which the former is the greater
	
	keyword arguments:
	a_list -- The list to be shuffled in order to check the quality of the shuffle.
	"""
	
	if type(a_list) != list:
		return "invalid argument"

	shuffle(a_list)
	greater = 0
	for i in range(len(a_list)-1):					#compares each pair of consecutive items
		if a_list[i+1] > a_list[i]:
			greater += 1
	return greater/float(len(a_list)-1)				#returns the quality

def average_quality(a_list, trials):
	"""
	use the quality function many times to find the average quality of the shuffle
	
	keyword arguments:
	a_list -- the list used to check the quality of the shuffle many times
	trials -- how many times the average_quality function will check the
	quality of the list for its average
	"""
	sum = 0
	for i in range(trials):
		sum += quality(a_list)						
	return sum/trials							#sums the quality of "trials" number of shuffles, then returns that sum divided by "trials"


if __name__ == "__main__":
	numbers = range(1, 21)
	greek = [" alpha ", " beta ", " gamma ", " delta ", " epsilon ", " zeta ", "eta",
	" theta ", " iota ", " kappa ", " lambda ", "mu"]

	print "A shuffle of the numbers one to twenty: \n", shuffle(numbers), "\n"
	print "A shuffle of the greek letters", greek, ": \n", shuffle(greek), "\n"
	print "the average quality of the shuffle when shuffling the list of numbers from zero to ninety-nine, one thousand times, is", average_quality(range(100), 1000)