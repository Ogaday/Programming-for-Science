def rsum(n):
	"""
	recursively find the sum of the integers of a list
	"""
	if len(n) == 0:
		return 0
	else:
		return n[0] + rsum(n[1:])

def enter_list(x):
	the_list = [x]
	while True:
		x = raw_input("==> ")
		if x.lower() == "done":
			print "The sum of your list is:"
			break
		else:
			try:
				the_list.append(float(x))
			except:
				print "Please enter value again"
	return the_list
		
if __name__ == "__main__":
	print "Welcome to the RECURSIVE SUM CALCULATOR\n"
	print "\nPrints the recursive sum of the first n positive integers. To start, enter an integer 'n'."
	while True:
		x = raw_input("==> ")
		if x.lower() == "q" or x.lower() == "quit":
			print "Thank you for using this program"
			break
		else:
			try:
				print rsum(range(1, int(x)+1))
			except:
				print "Please enter input again"
