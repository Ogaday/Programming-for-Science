print "AVERAGE CALCULATOR \nOgaday Willers Moore \n \nEnter numbers when prompted. Enter \"average\" to \nreturn the average of the numbers printed so far, \nand \"q\" or \"Q\" to quit."
sum = 0.0
count = 0

while True:
	try:
		input = raw_input("Enter command: \n==>")
		
		if input == "average":
			print "The average is %.2f" % (sum/count)
			sum = 0.0
			count = 0
		elif input.lower() == "q":
			break
		else:
			sum += float(input)
			count += 1

	except:
		print "Invalid Command! \n"