def rsum(n):
	"""
	recursively find the sum of the integers of a list
	"""
	if len(n) == 1:
		return n[0]
	elif len(n) == 0:
		return 0
	else:
		return n[0] + n[-1] + rsum(n[1:-1])

def enter_list():
	the_list = []
	while True:
		x = raw_input("==> ")
		if x.lower() == "q" or x.lower() == "quit":
			return
		if x.lower() == "done":
			break
		else:
			try:
				the_list.append(float(x))
			except:
				print "Please input value again"
	return the_list
	
if __name__ == "__main__":
	print "Welcome to the RECURSIVE SUM CALCULATOR\nTo start, enter each value of the list you would like to sum followed by enter. When you have finished, entering values, type 'done'. In order to quit at any time, type 'q' or 'quit'."
	while True:
		x = enter_list()
		if x == None:
			print "Thank you for using this program!"
			break
		else:
			print "The sum of your list is " + str(rsum(x)) + "\nBegin entering the next list to be summed, or type 'q' or 'quit' in order to quit."