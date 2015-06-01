def factorial(n):
	"""
	return the recursive factorial of n
	"""
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

if __name__ == "__main__":
	print """Welcome to the FACTORIAL CALCULATOR\n \nTo use the calculator, enter the number for which you want the factorial of, then press enter. In order to quit, type 'q' or 'quit'"""
	
	while True:
		x = raw_input("==> ")
		if x.lower() == "q" or x.lower() == "quit":
			print "Thank you for using this program"
			break
		else:
			try:
				print factorial(int(x))
			except:
				print "Please enter input again"